from sqlalchemy import text, insert, select, bindparam, update
from database.db import async_engine, sync_engine, async_session, sync_session
from database.ORM.models_orm import Base, UserOrm
from sqlalchemy.orm import joinedload, selectinload


class SyncOrm:

    @staticmethod
    def select_user(user_id: int) -> UserOrm:
        with sync_session() as session:
            query = select(UserOrm).where(UserOrm.id == user_id)
            result = session.execute(query)
            user = result.fetchall(UserOrm)
            return user
