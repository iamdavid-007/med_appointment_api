from fastapi import Depends, HTTPException, APIRouter
from schemas.patient import Patient, PatientCreate
from services.patient import PatientService

patient_router = APIRouter()

# Create a new patient
# List all patients
# Update a patient
# Get a patient by id
# Delete a patient

# Create a new patient
@patient_router.post("/", status_code=201)
async def create_patient(payload: PatientCreate):
    return PatientService.create_patient(payload)
    

# List all patients
@patient_router.get("/", status_code=200)
async def get_patients():
    return PatientService.get_patients()

# Update a patient
@patient_router.put("/{patient_id}", status_code=200)
async def update_patient(patient_id: int, payload: PatientCreate):
    return PatientService.update_patient(patient_id, payload)

# Get a patient by id
@patient_router.get("/{patient_id}", status_code=200)
async def get_patient(patient_id: int):
    return PatientService.get_patient_by_id(patient_id)

# Delete a patient
@patient_router.delete("/{patient_id}", status_code=200)
async def delete_patient(patient_id: int):
    return PatientService.delete_patient(patient_id)
    

