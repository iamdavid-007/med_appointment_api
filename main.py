import uvicorn
from fastapi import FastAPI
from routers import patient, doctor, appointment
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import medical_appointment_middleware
from logger import logger

app = FastAPI()

logger.info("===Starting App===")

app.include_router(patient.patient_router, prefix="/patients", tags=["patients"])
app.include_router(doctor.doctor_router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment.appointment_router, prefix="/appointments", tags=["appointments"])
app.add_middleware(BaseHTTPMiddleware, dispatch=medical_appointment_middleware)

@app.get("/welcome")
def index():
    return {"message": "welcome to our medical appointment system"}
