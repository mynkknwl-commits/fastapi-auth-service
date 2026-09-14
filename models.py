from sqlalchemy import String, DateTime,Date,Text,ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone,date
from database import Base

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

class Application(Base):
        __tablename__ = 'applications'
        id: Mapped[int] = mapped_column(primary_key=True, index=True)
        user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
        company: Mapped[str] = mapped_column(String)
        role: Mapped[str] = mapped_column(String)
        status: Mapped[str] = mapped_column(String, default="applied")  # applied/interview/offer/rejected
        applied_date: Mapped[date] = mapped_column(Date, nullable=False)
        follow_up_date: Mapped[date | None] = mapped_column(Date, nullable=True)
        notes: Mapped[str | None] = mapped_column(Text, nullable=True)
