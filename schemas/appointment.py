from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Appointment(BaseModel):
    id: Optional[int]
    date: datetime
    patient: int
    doctor: int