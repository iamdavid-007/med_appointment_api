from schemas.appointment import Appointment
from fastapi import HTTPException
from schemas.doctor import doctors
from schemas.patient import patients
from datetime import datetime

appointments = []

class AppointmentService:
    @staticmethod
    def create_appointment(patient_id: int):
        # Check if patient exists
        patient_exists = any(patient.id == patient_id for patient in patients)
        if not patient_exists:
            raise HTTPException(status_code=404, detail="Patient not found")
        doctor = None
        for d in doctors:
            if d.is_available:
                doctor = d
                break
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not available")
                
        appointment = Appointment(
            id = len(appointments) + 1,
            date = datetime.now(),
            patient = patient_id,
            doctor = doctor.id
        )

        doctor.is_available = False
        appointments.append(appointment)

        return {"message": "Appointment created successfully", "data": appointment}
    
    @staticmethod
    def complete_appointment(appointment_id: int):
        appointment = None
        for a in appointments:
            if a.id == appointment_id:
                appointment = a
                break
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        
        doctor = None
        for d in doctors:
            if d.id == appointment.doctor:
                doctor = d
                break
        
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor.is_available = True

        return {"message": "Appointment completed successfully", "data": appointment}
    
    @staticmethod
    def cancel_appointment(appointment_id: int):
        appointment = None
        for a in appointments:
            if a.id == appointment_id:
                appointment = a
                break
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        
        doctor = None
        for d in doctors:
            if d.id == appointment.doctor:
                doctor = d
                break
        
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor.is_available = True

        appointments.remove(appointment)

        return {"message": "Appointment cancelled successfully", "data": appointment}
    