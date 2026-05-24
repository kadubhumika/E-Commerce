from pydantic import BaseModel


class ProfileResponse(BaseModel):
    username: str
    first_name: str
    last_name: str
    phone: str
    address: str

    class Config:
        from_attributes = True


class ProfileUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    address: str