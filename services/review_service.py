from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.review import Review
from schemas.review import *


class ReviewService:

    @staticmethod
    async def add_review(
            db:AsyncSession,
            data:ReviewCreate
    ):

        existing=await db.execute(
            select(Review).where(
                Review.customer_id==data.customer_id,
                Review.product_id==data.product_id
            )
        )

        if existing.scalar_one_or_none():
            return None

        review=Review(
            **data.model_dump()
        )

        db.add(review)

        await db.commit()

        await db.refresh(review)

        return review


    @staticmethod
    async def get_reviews(
            db:AsyncSession,
            product_id:int
    ):

        result=await db.execute(
            select(Review).where(
                Review.product_id==product_id
            )
        )

        return result.scalars().all()