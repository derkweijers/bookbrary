from bookbrary.models import User
from werkzeug.security import generate_password_hash

from bookbrary.deps import db

class UserService:
    def create_user(self, username: str, password: str) -> User:
        user = User()
        user.username = username
        user.password = generate_password_hash(password=password)

        db.session.add(instance=user)
        db.session.commit()

        return user