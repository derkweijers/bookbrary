from .user_service import UserService
from .book_service import BookService

user_service = UserService()
book_service = BookService()

__all__ = ["user_service", "book_service"]
