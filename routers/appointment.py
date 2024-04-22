from fastapi import APIRouter, HTTPException, Depends
from services.appointment import AppointmentService
from schemas.appointment import Appointment

appointment_router = APIRouter()

@appointment_router.post("/", status_code=201)
async def create_appointment(patient_id: int):
    return AppointmentService.create_appointment(patient_id)

@appointment_router.put("/complete/{appointment_id}", status_code=200)
async def complete_appointment(appointment_id: int):
    return AppointmentService.complete_appointment(appointment_id)

@appointment_router.put("/cancel/{appointment_id}", status_code=200)
async def cancel_appointment(appointment_id: int):
    return AppointmentService.cancel_appointment(appointment_id)
