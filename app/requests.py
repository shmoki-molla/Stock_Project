from app.models import async_session
from app.models import User
from sqlalchemy import select, update, delete, text
import pandas as pd
from sqlalchemy.dialects.postgresql import array


async def set_user(tg_id: int, user_name: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(user_name=user_name, tg_id=tg_id, company=[]))
            await session.commit()


async def get_users():
    async with async_session() as session:
        users = await session.scalars(select(User.tg_id))
        users_id = users.all()
        return users_id


async def get_prices(table_name):
    async with async_session() as session:
        query = text(f"SELECT * FROM {table_name}")
        result = await session.execute(query)
        records = result.fetchall()
        columns = result.keys()
        df = pd.DataFrame(records, columns=columns)

        return df

async def get_companies():
    async with async_session() as session:
        query = text("SELECT company FROM companies")
        result = await session.execute(query)
        companies = result.fetchall()
        return companies

async def add_company_to_user(tg_id, new_company):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.company).where(User.tg_id == tg_id))
            user_company = result.scalar_one_or_none()
            print(tg_id)
            print(new_company)
            if user_company is None:
                user_company = []
            if new_company not in user_company:
                new_company_list = user_company + [new_company]
                print(new_company_list)

                await session.execute(update(User).where(User.tg_id == tg_id).values(company=new_company_list))
                await session.commit()
            else:
                pass

async def get_companies_from_user(tg_id):
    async with async_session() as session:
        result = await session.execute(select(User.company).where(User.tg_id == tg_id))
        user_company = result.scalar_one_or_none()
        return user_company



