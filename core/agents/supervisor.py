from core.state import PatientState

def process(state: PatientState, user_input: str) -> PatientState:
    print(f"\n[Supervisor] Auditing Triage output for clinical safety...")
    
    # In a full custom model, this would be a secondary classification model.
    # For now, we use a deterministic rule-based safety net.
    forbidden_terms = ["prescribe", "take pill", "dosage", "buy medicine"]
    guideline = state.risk_assessment.lower() if state.risk_assessment else ""
    
    is_safe = True
    for term in forbidden_terms:
        if term in guideline:
            is_safe = False
            print(f"[Supervisor WARNING] Blocked unsafe medical advice containing: '{term}'")
            break
            
    if not is_safe:
        # Override the unsafe output
        state.update_state("supervisor", {
            "risk_assessment": "SAFETY OVERRIDE: Cannot dispense medical advice. Please consult a doctor immediately.",
            "current_agent": "scheduler"
        })
    else:
        state.update_state("supervisor", {"current_agent": "scheduler"})
        print("[Supervisor Output] Safety check PASSED.")
        
    return state