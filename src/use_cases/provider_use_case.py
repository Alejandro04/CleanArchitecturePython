from typing import List
   
from src.domain.provider import Provider
from src.domain.provider_repository import ProviderRepository
   
class ProviderUseCase:
    def __init__(self, Provider_repository: ProviderRepository):
        self.Provider_repository = Provider_repository
   
    def create(self, Provider: Provider) -> Provider:
        return self.Provider_repository.create(Provider)
   
    def get_all(self) -> List[Provider]:
        return self.Provider_repository.get_all()
   
    def get_by_id(self, id: int) -> Provider:
        return self.Provider_repository.get_by_id(id)
   
    def update(self, id: int, Provider: Provider) -> Provider:
        return self.Provider_repository.update(id, Provider)
   
    def delete(self, id: int) -> None:
        return self.Provider_repository.delete(id)
