from sqlalchemy import String
from sqlalchemy.orm import  DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50), unique = True, nullable=False)
    score: Mapped[int] = mapped_column(nullable=False)

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="viewer", nullable=False)
