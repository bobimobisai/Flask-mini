from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base


class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[int] = mapped_column(default=0)
