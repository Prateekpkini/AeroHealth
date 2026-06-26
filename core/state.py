from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

@dataclass
class PatientState:
    session_id: str
    current_agent: str = "receptionist"
    agent_response: str = ""  # <-- THIS MUST BE HERE
    
    patient_name: Optional[str] = None
    raw_symptoms: Optional[str] = None
    language: str = "en" 
    
    priority_score: int = 0 
    recommended_department: Optional[str] = None
    risk_assessment: Optional[str] = None
    
    preferred_time: Optional[str] = None
    allocated_slot: Optional[str] = None
    workflow_complete: bool = False
    
    history: List[Dict[str, Any]] = field(default_factory=list)

    def update_state(self, agent_name: str, updates: Dict[str, Any]):
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.history.append({"agent": agent_name, "updates": updates})