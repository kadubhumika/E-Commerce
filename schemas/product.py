from decimal import Decimal
from pydantic import Field
from schemas.base import BaseSchema


class ProductCreate(BaseSchema):

    name:str
    description:str
    price:Decimal

    stock_quantity:int=Field(
        ge=0
    )

    image_url:str=""

    category_id:int

    brand:str=""

    rating:Decimal=0

    discount:int=Field(
        ge=0,
        le=100
    )


class ProductUpdate(BaseSchema):

    name:str|None=None
    description:str|None=None
    price:Decimal|None=None

    stock_quantity:int|None=None

    image_url:str|None=None

    category_id:int|None=None

    brand:str|None=None

    rating:Decimal|None=None

    discount:int|None=None


class ProductResponse(BaseSchema):

    product_id:int
    name:str
    description:str
    price:Decimal

    stock_quantity:int

    image_url:str

    category_id:int

    brand:str

    rating:Decimal

    discount:int