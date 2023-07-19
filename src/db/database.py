import sqlite3
from src.models.character import Character

DATABASE = "friends.db"
TABLE_NAME = "friends"


class SQLiteConnector:
    def __init__(self):
        self.database_name = DATABASE
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_name)
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados fechada com sucesso.")

    def read_all(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"SELECT * FROM {TABLE_NAME}")
                rows = cursor.fetchall()
                characters = []
                for row in rows:
                    character = Character(
                        name=row[1],
                        age=row[2],
                        sex=row[3],
                        season=row[4],
                        ocupation=row[5],
                        joke=row[6]
                    )
                    characters.append(character)
                return characters
            except Exception as e:
                print(f"Erro ao ler dados da tabela {TABLE_NAME}: {e}")
        else:
            print("Conexão com o banco de dados não estabelecida.")
            return []

    def get_by_name(self, name):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(
                    f"SELECT * FROM {TABLE_NAME} WHERE name=?", (name,))
                rows = cursor.fetchall()
                for row in rows:
                    character = Character(
                        name=row[1],
                        age=row[2],
                        sex=row[3],
                        season=row[4],
                        ocupation=row[5],
                        joke=row[6]
                    )
                return character
            except Exception as e:
                print(f"Não foi possível buscar {name}: {e}")
        else:
            print("Conexão com o banco de dados não estabelecida.")
            return None
