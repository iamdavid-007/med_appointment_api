from pydantic import BaseModel

# Doctors: id, name, specialization, phone, is_available (defaults to True)

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str

doctors: list[Doctor] = [
    Doctor(id=1, name="Dr. Olusegun", specialization="Cardiologist", phone="08022339870"),
    Doctor(id=2, name="Dr. Jonah", specialization="Dentist", phone="08041939871"),
    Doctor(id=3, name="Dr. David", specialization="Pediatrician", phone="08020060872"),
    Doctor(id=4, name="Dr. Damilola", specialization="Psycologist", phone="08020060872"),
]