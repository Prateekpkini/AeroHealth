from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    allocated_time = "10:30 AM" if state.priority_score == 3 else "04:00 PM"
    
    state.update_state("scheduler", {
        "allocated_slot": allocated_time, 
        "workflow_complete": True,
        "agent_response": f"📅 **Appointment Confirmed!**\n\nYour slot is reserved in {state.recommended_department} at **{allocated_time}**."
    })
    return state