from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegister(BaseModel):
    name:str
    email:EmailStr
    created_at:datetime
