from typing import List
   
from src.core.domain.user import User
from src.core.domain.user_repository import UserRepository
   
class UserUseCase:
    def __init__(self, User_repository: UserRepository):
        self.User_repository = User_repository
   
    def auth(self, username: str, password: str) -> User:
        return self.User_repository.auth(username, password)