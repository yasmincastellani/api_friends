from fastapi import APIRouter
from pydantic import BaseModel

routes = APIRouter()


class Character(BaseModel):
    name: str
    age: int
    sex: str
    season: int
    ocupation: str
    joke: str


@routes.get("/howyoudoin", response_model=Character, response_description="Esse endpoint retorna características do Joey", tags=["Joey"])
def joey():
    j = Character(
        name="Joey Tribbiani",
        age=28,
        sex="Masculino",
        ocupation="ator",
        season=3,
        joke="How you doing? 😏"
    )
    return j


@routes.get("/unagi", response_model=Character, response_description="Esse endpoint retorna características do Ross", tags=["Ross"])
def ross():
    r = Character(
        name="Ross Geller",
        age=31,
        sex="Masculino",
        ocupation="Paleontólogo e professor universitário",
        season=5,
        joke="Nós estávamos dando um tempo 😡"
    )
    return r


@routes.get("/rachelgreen", response_model=Character, response_description="Esse endpoint retorna características da Rachel", tags=["Rachel"])
def rachel():
    r = Character(
        name="Rachel Green",
        age=28,
        sex="Feminino",
        ocupation="Executiva de moda na Ralph Lauren",
        season=6,
        joke="Vou buscar um desses…desses…empregos 💼"
    )
    return r


@routes.get("/couldibemorefunny", response_model=Character, response_description="Esse endpoint retorna características do Chandler", tags=["Chandler"])
def chandler():
    c = Character(
        name="Chandler Bing",
        age=29,
        sex="Masculino",
        ocupation="Executivo em processamento de dados",
        season=6,
        joke="Na verdade, é Miss Chanandler Bong 😌"
    )
    return c


@routes.get("/cleaningfreak", response_model=Character, response_description="Esse endpoint retorna características da Monica", tags=["Monica"])
def monica():
    m = Character(
        name="Monica Geller",
        age=30,
        sex="Feminino",
        ocupation="Chef de cozinha",
        season=5,
        joke="Você faz parte do meu time! E meu time sempre vence! 🏆"
    )
    return m


@routes.get("/smellycat", response_model=Character, response_description="Esse endpoint retorna características da Phoebe", tags=["Phoebe"])
def phoebe():
    p = Character(
        name="Phoebe Buffay",
        age=32,
        sex="Feminino",
        ocupation="Massagista e musicista",
        season=4,
        joke="Smelly cat, smelly cat. What are they feeding you? Smelly cat, smelly cat… It’s not your fault. 🐱"
    )
    return p
