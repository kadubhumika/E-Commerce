from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Category
from models.base import Base
from schemas.category import CategoryCreate, CategoryUpdate

class CategoryService:
    @staticmethod
    async def list_categories(db: AsyncSession):
        result = await db.execute(select(Category).order_by(Category))
        return result.scalars().all()
    @staticmethod
    async def create_category(db: AsyncSession, data: CategoryCreate):
        new_category = Category(**data.model_dump())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

