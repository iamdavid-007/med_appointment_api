from schemas.doctor import Doctor, DoctorCreate, doctors
from fastapi import HTTPException

class DoctorService:
    @staticmethod
    def create_doctor(payload: DoctorCreate):
        new_doctor = Doctor(
            id = len(doctors) + 1,
            name = payload.name,
            specialization = payload.specialization,
            phone = payload.phone
        )
        doctors.append(new_doctor)
        return {"message": "Doctor created successfully", "data": new_doctor}
    
    @staticmethod
    def update_doctor(doctor_id: int, payload: DoctorCreate):
        current_doctor = None
        for doctor in doctors:
            if doctor.id == doctor_id:
                current_doctor = doctor
                break
        
        if not current_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        current_doctor.name = payload.name
        current_doctor.specialization = payload.specialization
        current_doctor.phone = payload.phone

        return {"message": "Doctor updated successfully", "data": current_doctor}
    
    @staticmethod
    def get_doctors():
        return {"message": "success", "data": doctors}
    
    @staticmethod
    def get_doctor_by_id(doctor_id: int):
        doctor = None
        for d in doctors:
            if d.id == doctor_id:
                doctor = d
                break
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return {"message": "success", "data": doctor}
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = None
        for d in doctors:
            if d.id == doctor_id:
                doctor = d
                break
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctors.remove(doctor)
        return {"message": "Doctor deleted successfully"}
    
    @staticmethod   
    def set_availability(doctor_id: int, is_available: bool):
        doctor = None
        for d in doctors:
            if d.id == doctor_id:
                doctor = d
                break
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        doctor.is_available = is_available
        if is_available:
            return {"message": "Doctor is now available", "data": doctor}
        else:
            return {"message": "Doctor is unavailable", "data": doctor}
        
        
    