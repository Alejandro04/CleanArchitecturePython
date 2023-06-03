import mysql.connector
from mysql.connector import errorcode

from src.domain.provider import Provider
from src.domain.provider_repository import ProviderRepository
from typing import List

class ProviderRepositoryMySQL(ProviderRepository):
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="shipping",
        )

    def create(self, Provider: Provider) -> Provider:
        cursor = self.cnx.cursor()
        query = "INSERT INTO providers (name, email, address, phone) VALUES (%s, %s, %s, %s)"
        values = (Provider.name, Provider.email, Provider.address, Provider.phone)
        cursor.execute(query, values)
        self.cnx.commit()
        Provider.id = cursor.lastrowid
        cursor.close()
        return Provider

    def get_all(self) -> List[Provider]:
        cursor = self.cnx.cursor()
        query = "SELECT id, name, email, address, phone FROM providers"
        cursor.execute(query)
        Provideres = []
        for (id, name, email, address, phone) in cursor:
            Provideres.append(Provider(id=id, name=name, email=email, address=address, phone=phone))
        cursor.close()
        return Provideres

    def get_by_id(self, id: int) -> Provider:
        cursor = self.cnx.cursor()
        query = "SELECT id, name, email, address, phone FROM providers WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return Provider(id=result[0], name=result[1], email=result[2], address=result[3], phone=result[4])

    def update(self, id: int, Provider: Provider) -> Provider:
        cursor = self.cnx.cursor()
        query = "UPDATE providers SET name = %s, email = %s, address = %s, phone = %s WHERE id = %s"
        values = (Provider.name, Provider.email, Provider.address, Provider.phone, id)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()
        Provider.id = id
        return Provider

    def delete(self, id: int) -> None:
        pass
