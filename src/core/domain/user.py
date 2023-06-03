class User:
    def __init__(self, id, username, password):
        self.validate_username(username)
        self.validate_password(password)

        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def from_dict(data):
        id = data.get('id')
        username = data.get('username')
        password = data.get('password')
        return User(id, username, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

    def validate_username(self, username):
        if not username:
            raise ValueError("Username is required")

    def validate_password(self, password):
        if not password:
            raise ValueError("Password is required")