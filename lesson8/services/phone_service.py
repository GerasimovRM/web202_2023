from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Phone


class PhoneService:
    @staticmethod
    async def get_all_phones_by_user(user_id: int,
                                     session: AsyncSession):
        query = await session.execute(select(Phone).where(Phone.user_id == user_id))
        phones = query.scalars().all()
        return phones