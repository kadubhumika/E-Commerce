from schemas.base import BaseSchema

# --- CATEGORY SCHEMAS ---
class CategoryCreate(BaseSchema):
    name: str
    description: str | None = None

class CategoryUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None

class CategoryResponse(BaseSchema):
    category_id: int
    name: str
    description: str | None = None