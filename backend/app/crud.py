from sqlalchemy import select
from .models import Review
from .db import AsyncSessionLocal

async def create_review(contact_number, user_name, product_name, product_review):
    async with AsyncSessionLocal() as session:
        review = Review(
            contact_number=contact_number,
            user_name=user_name,
            product_name=product_name,
            product_review=product_review
        )
        session.add(review)
        await session.commit()
        return review

async def list_reviews():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Review))
        return result.scalars().all()
