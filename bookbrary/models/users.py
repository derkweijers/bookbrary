from sqlalchemy import func
from bookbrary.deps import db
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    # attributes with created_at and updated_at are added to the User model
    created_at: Mapped[str] = mapped_column(
        default=func.now(), server_default=func.now()
    )
    updated_at: Mapped[str] = mapped_column(
        default=func.now(), onupdate=func.now(), server_default=func.now()
    )
