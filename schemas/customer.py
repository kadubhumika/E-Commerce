from schemas.base import BaseSchema

class CustomerCreate(BaseSchema):
    user_id: int
    username: str
    first_name: str
    last_name: str
    phone: str
    address: str

class CustomerUpdate(BaseSchema):
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    address: str | None = None

class CustomerResponse(BaseSchema):
    customer_id: int
    user_id: int
    username: str
    first_name: str
    last_name: str
    phone: str
    address: str