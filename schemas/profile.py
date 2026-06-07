from pydantic import BaseModel
from typing import Optional


class ProfileResponse(BaseModel):
    customer_id:int

    username:str

    first_name:str
    last_name:str
    phone:str
    address:str

    city:str
    state:str
    country:str
    pincode:str



    profile_image: Optional[str] = None

    class Config:
        from_attributes=True


class ProfileUpdate(BaseModel):

    first_name:str=""
    last_name:str=""
    phone:str=""
    address:str=""

    city:str=""
    state:str=""
    country:str=""
    pincode:str=""

    profile_image: Optional[str] = None