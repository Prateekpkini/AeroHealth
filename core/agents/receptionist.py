from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    if not state.patient_name:
        state.update_state("receptionist", {
            "patient_name": user_input, 
            "current_agent": "receptionist",
            "agent_response": f"Thank you, {user_input}. Please describe your symptoms in detail."
        })
    else:
        state.update_state("receptionist", {
            "raw_symptoms": user_input, 
            "current_agent": "triage",
            "agent_response": "Symptoms logged. Running Edge-Native Triage protocol..."
        })
    return state