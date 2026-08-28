from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50), unique = True, nullable=False)
    score: Mapped[int] = mapped_column(nullable=False)
    class_id: Mapped[int | None] = mapped_column(ForeignKey("classes.id"), nullable=True)

    class_info: Mapped["ClassModel"] = relationship(back_populates="students")
class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="viewer", nullable=False)

class ClassModel(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] =mapped_column(String(50), unique=True, nullable=False)

    students:Mapped[list["StudentModel"]] = relationship(back_populates="class_info")
