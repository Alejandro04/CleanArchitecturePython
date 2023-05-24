from src.domain.provider import Provider

def test_provider_attributes():
    provider = Provider(1, "Provider 1", "provider1@example.com", "123 Main St", "123-456-7890")
    assert provider.id == 1
    assert provider.name == "Provider 1"
    assert provider.email == "provider1@example.com"
    assert provider.address == "123 Main St"
    assert provider.phone == "123-456-7890"
from src.domain.validate_email_format import validate_email_format
from src.domain.provider import Provider

def test_provider_initialization():
    id = 1
    name = "Provider 1"
    email = "provider1@example.com"
    address = "123 Main St"
    phone = "123-456-7890"

    provider = Provider(id, name, email, address, phone)

    assert provider.id == id
    assert provider.name == name
    assert provider.email == email
    assert provider.address == address
    assert provider.phone == phone

def test_provider_from_dict():
    data = {
        'id': 1,
        'name': 'Provider 1',
        'email': 'provider1@example.com',
        'address': '123 Main St',
        'phone': '123-456-7890'
    }

    provider = Provider.from_dict(data)

    assert provider.id == data['id']
    assert provider.name == data['name']
    assert provider.email == data['email']
    assert provider.address == data['address']
    assert provider.phone == data['phone']

def test_provider_to_dict():
    id = 1
    name = "Provider 1"
    email = "provider1@example.com"
    address = "123 Main St"
    phone = "123-456-7890"

    provider = Provider(id, name, email, address, phone)

    data = provider.to_dict()

    assert data['id'] == id
    assert data['name'] == name
    assert data['email'] == email
    assert data['address'] == address
    assert data['phone'] == phone

def test_provider_validate_name():
    provider = Provider(1, "Provider 1", "provider1@example.com", "123 Main St", "123-456-7890")

    # Prueba con un nombre válido
    provider.validate_name("John Doe")

    # Prueba con un nombre vacío
    try:
        provider.validate_name("")
        assert False, "Se esperaba un ValueError al proporcionar un nombre vacío"
    except ValueError:
        pass

def test_provider_validate_email():
    provider = Provider(1, "Provider 1", "provider1@example.com", "123 Main St", "123-456-7890")

    # Prueba con un email válido
    provider.validate_email("test@example.com")

    # Prueba con un email vacío
    try:
        provider.validate_email("")
        assert False, "Se esperaba un ValueError al proporcionar un email vacío"
    except ValueError:
        pass

    # Prueba con un email con formato inválido
    try:
        provider.validate_email("testexample.com")
        assert False, "Se esperaba un ValueError al proporcionar un email con formato inválido"
    except ValueError:
        pass

def test_provider_validate_address():
    provider = Provider(1, "Provider 1", "provider1@example.com", "123 Main St", "123-456-7890")

    # Prueba con una dirección válida
    provider.validate_address("456 Elm St")

    # Prueba con una dirección vacía
    try:
        provider.validate_address("")
        assert False, "Se esperaba un ValueError al proporcionar una dirección vacía"
    except ValueError:
        pass