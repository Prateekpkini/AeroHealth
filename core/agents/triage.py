from core.state import PatientState
from core.utils.rag_engine import TriageRAG

# Initialize the RAG engine at the module level so it only loads into memory once
rag = TriageRAG()

def process(state: PatientState, user_input: str) -> PatientState:
    print(f"[Triage] Running semantic vector search on symptoms: '{state.raw_symptoms}'")
    
    # Query the local vector database instead of using if/else rules
    rag_result = rag.search(state.raw_symptoms)
    
    priority = rag_result["priority"]
    dept = rag_result["department"]
    guideline = rag_result["guideline"]

    state.update_state("triage", {
        "priority_score": priority,
        "recommended_department": dept,
        "risk_assessment": guideline,
        "current_agent": "supervisor"
    })
    
    print(f"[Triage Output] Match Found! Priority {priority} -> {dept}.")
    print(f"[Triage Clinical Note] {guideline}")
    return state