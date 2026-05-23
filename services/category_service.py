from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.category import Category  # Make sure the import path is exact
from schemas.category import CategoryCreate

class CategoryService:
    @staticmethod
    async def list_categories(db: AsyncSession):

        result = await db.execute(select(Category).order_by(Category.name))
        return result.scalars().all()

    @staticmethod
    async def create_category(db: AsyncSession, data: CategoryCreate):
        new_category = Category(**data.model_dump())
        db.add(new_category)
        await db.commit()
        await db.refresh(new_category)
        return new_category
