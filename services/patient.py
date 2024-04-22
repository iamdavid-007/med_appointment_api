from schemas.patient import Patient, PatientCreate, patients
from fastapi import HTTPException

class PatientService:
    @staticmethod
    def create_patient(payload: PatientCreate):
        new_patient = Patient(
            id = len(patients) + 1,
            name = payload.name,
            age = payload.age,
            sex = payload.sex,
            weight = payload.weight,
            height = payload.height,
            phone = payload.phone
        )
        patients.append(new_patient)
        return {"message": "Patient created successfully", "data": new_patient}
    
    @staticmethod
    def update_patient(patient_id: int, payload: PatientCreate):
        current_patient = None
        for patient in patients:
            if patient.id == patient_id:
                current_patient = patient
                break
        
        if not current_patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        current_patient.name = payload.name
        current_patient.age = payload.age
        current_patient.sex = payload.sex
        current_patient.weight = payload.weight
        current_patient.height = payload.height
        current_patient.phone = payload.phone

        return {"message": "Patient updated successfully", "data": current_patient}
    
    @staticmethod
    def get_patients():
        return {"message": "success", "data": patients}
    
    @staticmethod
    def get_patient_by_id(patient_id: int):
        patient = None
        for p in patients:
            if p.id == patient_id:
                patient = p
                break
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return {"message": "success", "data": patient}
    
    @staticmethod
    def delete_patient(patient_id: int):
        patient = None
        for p in patients:
            if p.id == patient_id:
                patient = p
                break
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        patients.remove(patient)
        return {"message": "Patient deleted successfully"}