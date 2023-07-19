from fastapi import APIRouter
from src.models.character import Character
from src.db.database import SQLiteConnector
from typing import List

routes = APIRouter()

connector = SQLiteConnector()


@routes.get("/all", response_model=List[Character], response_description="Esse endpoint retorna todos os personagens",
            tags=["All"])
def get_all():
    connector.connect()
    characters = connector.read_all()
    connector.close()
    return characters


@routes.get("/character", response_model=Character,
            response_description="Esse endpoint retorna características do Joey", tags=["Joey"])
def joey(character: str):
    connector.connect()
    character = connector.get_by_name(character)
    print(character)
    connector.close()
    return character
