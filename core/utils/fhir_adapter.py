import uuid
import datetime
from core.state import PatientState

class FHIRAdapter:
    """Converts internal PatientState into FHIR R4 compliant JSON resources."""
    
    @staticmethod
    def create_appointment_resource(state: PatientState) -> dict:
        """Generates a FHIR Appointment Resource."""
        
        # In a real system, you'd look up the patient's ABHA ID here
        patient_reference = f"Patient/{uuid.uuid4().hex[:8]}" 
        
        # Calculate a mock start time based on the allocated slot for today
        today = datetime.date.today()
        # For simplicity, assuming the slot is something like "10:30 AM"
        # In a robust system, you'd parse this properly. 
        # Here we just use a generic timestamp for the demo
        timestamp = f"{today}T10:30:00Z" 

        fhir_resource = {
            "resourceType": "Appointment",
            "status": "booked",
            "serviceCategory": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/service-category",
                            "code": "17", # Generic code for General Practice / Outpatient
                            "display": "General Practice"
                        }
                    ]
                }
            ],
            "specialty": [
                {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "display": state.recommended_department
                        }
                    ]
                }
            ],
            "appointmentType": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0276",
                        "code": "ROUTINE",
                        "display": "Routine appointment"
                    }
                ]
            },
            "reasonCode": [
                {
                    "text": state.raw_symptoms
                }
            ],
            "priority": state.priority_score,
            "description": state.risk_assessment,
            "start": timestamp,
            "participant": [
                {
                    "actor": {
                        "reference": patient_reference,
                        "display": state.patient_name
                    },
                    "status": "accepted"
                }
            ]
        }
        
        return fhir_resource