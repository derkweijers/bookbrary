from bookbrary.deps import db
from sqlalchemy.orm import Mapped, mapped_column


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    genre: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()
