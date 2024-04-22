from fastapi import APIRouter, HTTPException
from services.doctor import DoctorService
from schemas.doctor import DoctorCreate

doctor_router = APIRouter()

# Create a new doctor
# list all doctors
# Update a doctor
# Get a doctor by id
# Delete a doctor

@doctor_router.post("/", status_code=201)
async def create_doctor(payload: DoctorCreate):
    return DoctorService.create_doctor(payload)

@doctor_router.get("/", status_code=200)
async def get_doctors():
    return DoctorService.get_doctors()

@doctor_router.put("/{doctor_id}", status_code=200)
async def update_doctor(doctor_id: int, payload: DoctorCreate):
    return DoctorService.update_doctor(doctor_id, payload)

@doctor_router.get("/{doctor_id}", status_code=200)
async def get_doctor(doctor_id: int):
    return DoctorService.get_doctor_by_id(doctor_id)

@doctor_router.delete("/{doctor_id}", status_code=200)
async def delete_doctor(doctor_id: int):
    return DoctorService.delete_doctor(doctor_id)

@doctor_router.put("/{doctor_id}/set-availability", status_code=200)
async def set_availability(doctor_id: int, is_available: bool):
    return DoctorService.set_availability(doctor_id, is_available)
