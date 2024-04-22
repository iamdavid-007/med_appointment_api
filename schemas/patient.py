from pydantic import BaseModel

# Patient: id, name, age, sex, weight, height, phone
class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

patients: list[Patient] = [
    Patient(id=1, name="Damilola Adebayo", age=25, sex="female", weight=60.0, height=1.6, phone="08022339870"),
    Patient(id=2, name="Kayode Adebanjo", age=30, sex="male", weight=70.0, height=1.7, phone="08041939871"),
    Patient(id=3, name="Bola Adewale", age=35, sex="male", weight=76.5, height=1.6, phone="08020060872"),
]