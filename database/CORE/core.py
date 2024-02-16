from sqlalchemy import text, insert, select, bindparam, update
from database.db import async_engine, sync_engine, async_session, sync_session
from database.ORM.models_orm import Base, UserOrm


def create_table(drop_table: bool = False):
    if drop_table is True:
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
    else:
        Base.metadata.create_all(sync_engine)


class AsyncCore:
    async def insert_user(user_name: str):
        async with async_engine.connect() as conn:
            stmt = text('INSERT INTO "users" (username) VALUES (:user_name)')
            query = stmt.bindparams(user_name=user_name)
            await conn.execute(query)
            await conn.commit()
