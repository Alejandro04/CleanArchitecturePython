class Provider:
    def __init__(self, id, name, email, address, phone):
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