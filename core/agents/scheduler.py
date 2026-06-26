from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    print(f"[Scheduler] Checking slots for {state.recommended_department}...")
    allocated_time = "10:30 AM" if state.priority_score == 3 else "04:00 PM"
    
    state.update_state("scheduler", {"allocated_slot": allocated_time, "workflow_complete": True})
    print(f"[Scheduler Output] Appointment confirmed at {allocated_time}.")
    return state