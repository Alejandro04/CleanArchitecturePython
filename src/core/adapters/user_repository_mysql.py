import mysql.connector
from mysql.connector import errorcode

from src.core.domain.user import User
from src.core.domain.user_repository import UserRepository
from typing import List

class UserRepositoryMySQL(UserRepository):
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="shipping",
        )

    def auth(self, username: str, password: str) -> User:
        cursor = self.cnx.cursor()
        query = "SELECT * from users WHERE username = %s and password = %s"
        values = (username,password,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return User(id=result[0], username=result[1], password=result[2])