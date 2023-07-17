from fastapi import APIRouter
from src.models.character import Character
from src.db.database import SQLiteConnector
from typing import List

routes = APIRouter()

connector = SQLiteConnector()


@routes.get("/all", response_model=List[Character], response_description="Esse endpoint retorna todos os personagens", tags=["All"])
def all():
    connector.connect()
    characters = connector.read_all()
    connector.close()
    return characters


@routes.get("/howyoudoin", response_model=Character, response_description="Esse endpoint retorna características do Joey", tags=["Joey"])
def joey():
    connector.connect()
    character = connector.get_by_name("Joey Tribbiani")
    print(character)
    connector.close()
    return character


@routes.get("/unagi", response_model=Character, response_description="Esse endpoint retorna características do Ross", tags=["Ross"])
def ross():
    connector.connect()
    character = connector.get_by_name("Ross Geller")
    print(character)
    connector.close()
    return character


@routes.get("/rachelgreen", response_model=Character, response_description="Esse endpoint retorna características da Rachel", tags=["Rachel"])
def rachel():
    connector.connect()
    character = connector.get_by_name("Rachel Green")
    print(character)
    connector.close()
    return character


@routes.get("/couldibemorefunny", response_model=Character, response_description="Esse endpoint retorna características do Chandler", tags=["Chandler"])
def chandler():
    connector.connect()
    character = connector.get_by_name("Chandler Bing")
    print(character)
    connector.close()
    return character
    

@routes.get("/cleaningfreak", response_model=Character, response_description="Esse endpoint retorna características da Monica", tags=["Monica"])
def monica():
    connector.connect()
    character = connector.get_by_name("Monica Geller")
    print(character)
    connector.close()
    return character


@routes.get("/smellycat", response_model=Character, response_description="Esse endpoint retorna características da Phoebe", tags=["Phoebe"])
def phoebe():
    connector.connect()
    character = connector.get_by_name("Phoebe Buffay")
    print(character)
    connector.close()
    return character
