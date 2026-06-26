import streamlit as st
import uuid
from core.state import PatientState
from core.orchestrator import AeroHealthOrchestrator
from core.utils.fhir_adapter import FHIRAdapter

# Page Configuration
st.set_page_config(page_title="AeroHealth AI", page_icon="🏥", layout="centered")
st.title("🏥 AeroHealth AI")
st.caption("A Cloud-Agnostic Multi-Agent Engine for Federated Healthcare")

# 1. Initialize Backend State in the Web Session
if "state" not in st.session_state:
    st.session_state.state = PatientState(session_id=str(uuid.uuid4()))
    st.session_state.orchestrator = AeroHealthOrchestrator()
    st.session_state.chat_history = [{"role": "assistant", "content": "Welcome to the clinic! What is your full name?"}]

# 2. Render Chat History
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 3. Handle User Input
if not st.session_state.state.workflow_complete:
    if prompt := st.chat_input("Type your response here..."):
        
        # Display user message instantly
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Processing..."):
            # Step A: Route user input to the Receptionist
            st.session_state.state = st.session_state.orchestrator.route(st.session_state.state, prompt)
            if st.session_state.state.agent_response:
                st.session_state.chat_history.append({"role": "assistant", "content": st.session_state.state.agent_response})
            
            # Step B: Auto-run background agents (Triage -> Supervisor -> Scheduler)
            while st.session_state.state.current_agent != "receptionist" and not st.session_state.state.workflow_complete:
                st.session_state.state = st.session_state.orchestrator.route(st.session_state.state, "")
                if st.session_state.state.agent_response:
                    st.session_state.chat_history.append({"role": "assistant", "content": st.session_state.state.agent_response})
        
        # Refresh UI to show new messages
        st.rerun()

# 4. Display Interoperability Data upon completion
if st.session_state.state.workflow_complete:
    st.success("Workflow Complete! Data synchronized securely.")
    
    fhir_data = FHIRAdapter.create_appointment_resource(st.session_state.state)
    with st.expander("View FHIR R4 JSON Payload (ABDM Compliant)", expanded=False):
        st.json(fhir_data)
        
    if st.button("Start New Patient Session"):
        st.session_state.clear()
        st.rerun()