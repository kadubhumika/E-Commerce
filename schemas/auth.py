from pydantic import EmailStr
from schemas.base import BaseSchema

class UserRegister(BaseSchema):
    email: EmailStr
    password: str
    username: str # Handled inside routers to create Customer link simultaneously

class UserLogin(BaseSchema):
    email: EmailStr
    password: str

class TokenResponse(BaseSchema):
    access_token: str
    token_type: str

class UserResponse(BaseSchema):
    id: int
    email: EmailStr