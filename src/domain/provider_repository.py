from abc import ABC, abstractmethod
from typing import List

from src.domain.provider import Provider

class ProviderRepository(ABC):
    @abstractmethod
    def create(self, Provider: Provider) -> Provider:
        pass

    @abstractmethod
    def get_all(self) -> List[Provider]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Provider:
        pass

    @abstractmethod
    def update(self, id: int, Provider: Provider) -> Provider:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
