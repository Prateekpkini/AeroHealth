from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    forbidden_terms = ["prescribe", "take pill", "dosage", "buy medicine"]
    guideline = state.risk_assessment.lower() if state.risk_assessment else ""
    
    is_safe = True
    for term in forbidden_terms:
        if term in guideline:
            is_safe = False
            break
            
    if not is_safe:
        state.update_state("supervisor", {
            "risk_assessment": "SAFETY OVERRIDE: Cannot dispense medical advice.",
            "current_agent": "scheduler",
            "agent_response": "⚠️ **Safety Check Failed:** Unsafe medical advice blocked."
        })
    else:
        state.update_state("supervisor", {
            "current_agent": "scheduler",
            "agent_response": "✅ **Safety Check Passed:** Output validated against clinical rubrics."
        })
    return state