from abc import ABC, abstractmethod
from typing import List

from src.core.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def auth(self, username: str, password: str) -> User:
        pass
