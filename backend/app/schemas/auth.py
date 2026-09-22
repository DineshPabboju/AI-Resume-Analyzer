from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    type: str
    exp: str
    
class TokenData(BaseModel):
    id: str | None = None
    