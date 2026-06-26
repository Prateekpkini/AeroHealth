from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    print(f"[Receptionist] Input: '{user_input}'")
    if not state.patient_name:
        state.update_state("receptionist", {"patient_name": user_input, "current_agent": "receptionist"})
        print("[Receptionist Output] Thank you. Please describe your symptoms.")
    else:
        state.update_state("receptionist", {"raw_symptoms": user_input, "current_agent": "triage"})
        print("[Receptionist Output] Symptoms logged. Transferring to Triage.")
    return state