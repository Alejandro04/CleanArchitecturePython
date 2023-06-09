from src.domain.validate_email_format import validate_email_format

class Provider:
    def __init__(self, id, name, email, address, phone):
        self.validate_name(name)
        self.validate_email(email)
        self.validate_address(address)

        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    @staticmethod
    def from_dict(data):
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')
        return Provider(id, name, email, address, phone)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone': self.phone
        }

    def validate_name(self, name):
        if not name:
            raise ValueError("Name is required.")

    def validate_email(self, email):
        if not email:
            raise ValueError("Email is required.")
        if not validate_email_format(email):
            raise ValueError("Invalid email format.")

    def validate_address(self, address):
        if not address:
            raise ValueError("Address is required.")