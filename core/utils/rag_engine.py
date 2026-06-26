import pandas as pd
import faiss
import os
from sentence_transformers import SentenceTransformer

class TriageRAG:
    def __init__(self):
        print("[System] Loading local Sentence Transformer model... (This may take a moment on first run)")
        # Using a very small, fast, open-source model perfect for edge devices
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Load the knowledge base
        csv_path = os.path.join(os.path.dirname(__file__), '../../data/vector_db/medical_guidelines.csv')
        self.kb = pd.read_csv(csv_path)
        
        # Create Embeddings (converting text to numbers)
        print("[System] Indexing medical guidelines into FAISS Vector DB...")
        symptom_texts = self.kb['symptom_keywords'].tolist()
        self.embeddings = self.model.encode(symptom_texts)
        
        # Build the FAISS Index for blazing fast search
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)

    def search(self, patient_symptoms: str):
        """Finds the closest matching medical guideline based on the patient's symptoms."""
        query_vector = self.model.encode([patient_symptoms])
        
        # Search the index (k=1 means return the single closest match)
        distances, indices = self.index.search(query_vector, k=1)
        
        best_match_idx = indices[0][0]
        match_data = self.kb.iloc[best_match_idx]
        
        return {
            "department": match_data['department'],
            "priority": int(match_data['priority']),
            "guideline": match_data['clinical_guideline']
        }