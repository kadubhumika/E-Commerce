from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import *
from schemas import *
from schemas.product import ProductCreate, ProductUpdate


class ProductService:
    @staticmethod
    async def list_products(db: AsyncSession):
        result = await db.execute(select(Product))
        return result.scalars().all()
    @staticmethod
    async def create_product(db: AsyncSession, data:ProductCreate):
        new_prod = Product(**data.model_dump())
        db.add(new_prod)
        await db.commit()
        await db.refresh(new_prod)
        return new_prod
    @staticmethod
    async def update_product(db: AsyncSession, prod_id:int, data:ProductUpdate):
        result = await db.execute(select(Product).where(Product.product_id == prod_id))
        db_prod = result.scalar_one_or_none()
        if not db_prod:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(db_prod, key, value)

        await db.commit()
        await db.refresh(db_prod)
        return db_prod
