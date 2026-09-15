from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegister(BaseModel):
    name:str
    email:EmailStr
    password: str
    created_at:datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class User(BaseModel):
    name: str
    email: EmailStr
    created_at: datetime
    