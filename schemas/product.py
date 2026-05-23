from decimal import Decimal

from pydantic import Field

from schemas.base import BaseSchema

class ProductCreate(BaseSchema):
    name: str
    description: str
    price: Decimal
    stock: int = Field(
        ge=0
    )
    category_id: int

class ProductUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    stock: int = Field(
        ge=0
    )
    category_id: int | None = None

class ProductResponse(BaseSchema):
    product_id: int
    name: str
    description: str
    price: Decimal
    stock: int = Field(
        ge=0
    )
    category_id: int