import uuid
from core.state import PatientState
from core.orchestrator import AeroHealthOrchestrator

def run_simulation():
    orchestrator = AeroHealthOrchestrator()
    state = PatientState(session_id=str(uuid.uuid4()))
    
    print("--- AeroHealth AI Session Started ---")
    print("Agent: Welcome! What is your full name?")
    
    state = orchestrator.route(state, user_input="Prateek Kini")
    state = orchestrator.route(state, user_input="I have sharp chest pain.")
    
    # Auto-run triage and scheduler
    state = orchestrator.route(state, user_input="")
    state = orchestrator.route(state, user_input="")

    print("\n--- Final Audit Trail ---")
    for log in state.history:
        print(f"[{log['agent'].upper()}]: {log['updates']}")

if __name__ == "__main__":
    run_simulation()