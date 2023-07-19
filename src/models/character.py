from pydantic import BaseModel


class Character(BaseModel):
    name: str
    age: int
    sex: str
    season: int
    ocupation: str
    joke: str
