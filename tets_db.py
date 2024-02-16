from database.CORE.core import AsyncCore, create_table
from database.ORM.models_orm import UserOrm, Base
import asyncio

create_table(drop_table=True)

# async def main():
#     await AsyncCore.insert_user(user_name="Bob")


# asyncio.run(main())
