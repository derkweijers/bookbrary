from bookbrary.deps import db
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column()
    updated_at: Mapped[str] = mapped_column()

