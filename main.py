import uuid
import json
from core.state import PatientState
from core.orchestrator import AeroHealthOrchestrator
from core.utils.fhir_adapter import FHIRAdapter

def run_interactive_session():
    orchestrator = AeroHealthOrchestrator()
    state = PatientState(session_id=str(uuid.uuid4()))
    
    print("="*50)
    print(" 🏥 AEROHEALTH AI - CLINICAL TERMINAL ")
    print("="*50)
    
    # The Receptionist makes the first move
    user_input = ""
    state = orchestrator.route(state, user_input)
    
    # Interactive Chat Loop
    while not state.workflow_complete:
        # Only ask for user input if the current agent is the receptionist
        if state.current_agent == "receptionist":
            user_input = input("\n👤 You: ")
        else:
            # For internal agents (Triage, Supervisor, Scheduler), pass empty input 
            user_input = ""
            
        state = orchestrator.route(state, user_input)

    print("\n" + "="*50)
    print(" 📄 GENERATING FHIR R4 APPOINTMENT RESOURCE")
    print("="*50)
    
    fhir_data = FHIRAdapter.create_appointment_resource(state)
    print(json.dumps(fhir_data, indent=2))

if __name__ == "__main__":
    run_interactive_session()