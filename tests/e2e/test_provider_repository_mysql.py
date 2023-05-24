from src.domain.provider import Provider
from src.adapters.provider_repository_mysql import ProviderRepositoryMySQL

def test_provider_repository_integration():
    # Crear una instancia del repositorio
    repository = ProviderRepositoryMySQL()

    # Crear un nuevo proveedor con una dirección válida
    provider = Provider(id=None, name="Provider 50", email="provider50@example.com", address="add 50 50 50 add", phone="123-456-7890")
    created_provider = repository.create(provider)

    # Verificar que se haya asignado un ID al proveedor
    assert created_provider.id is not None

    # Obtener todos los proveedores del repositorio
    providers = repository.get_all()

    # Verificar que el proveedor creado esté en la lista de proveedores
    assert created_provider.to_dict() in [p.to_dict() for p in providers]

    # Actualizar el proveedor
    updated_provider = Provider(id=created_provider.id, name="Provider Updated", email="updated@example.com", address="456 Elm St", phone="987-654-3210")
    repository.update(created_provider.id, updated_provider)

    # Obtener nuevamente el proveedor por ID después de la actualización
    retrieved_provider = repository.get_by_id(created_provider.id)

    # Verificar que los atributos del proveedor hayan sido actualizados
    assert retrieved_provider.name == updated_provider.name
    assert retrieved_provider.email == updated_provider.email
    assert retrieved_provider.address == updated_provider.address
    assert retrieved_provider.phone == updated_provider.phone
