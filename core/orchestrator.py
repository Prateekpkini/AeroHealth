from core.state import PatientState
import importlib

class AeroHealthOrchestrator:
    def __init__(self):
        self.agent_registry = {
            "receptionist": "core.agents.receptionist.process",
            "triage": "core.agents.triage.process",
            "scheduler": "core.agents.scheduler.process"
        }

    def route(self, state: PatientState, user_input: str) -> PatientState:
        if state.workflow_complete:
            print("Workflow complete.")
            return state

        current_agent = state.current_agent
        module_path, func_name = self.agent_registry[current_agent].rsplit(".", 1)
        module = importlib.import_module(module_path)
        agent_function = getattr(module, func_name)

        print(f"\n[Orchestrator] Routing to: {current_agent.upper()}")
        return agent_function(state, user_input)