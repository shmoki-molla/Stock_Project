from app.models import async_session
from app.models import User
from sqlalchemy import select, update, delete


async def set_user(tg_id: int, user_name: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(user_name=user_name, tg_id=tg_id, company='AAPL'))
            await session.commit()


async def get_users():
    async with async_session() as session:
        users = await session.scalars(select(User.tg_id))
        users_id = users.all()
        return users_id
