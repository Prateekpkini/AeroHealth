from core.state import PatientState
from core.utils.rag_engine import TriageRAG

rag = TriageRAG()

def process(state: PatientState, user_input: str) -> PatientState:
    rag_result = rag.search(state.raw_symptoms)
    
    priority = rag_result["priority"]
    dept = rag_result["department"]
    guideline = rag_result["guideline"]

    msg = f"**Triage Complete:** Priority {priority}\n\n**Department:** {dept}\n\n**Note:** {guideline}"

    state.update_state("triage", {
        "priority_score": priority,
        "recommended_department": dept,
        "risk_assessment": guideline,
        "current_agent": "supervisor",
        "agent_response": msg
    })
    return state