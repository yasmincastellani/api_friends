from fastapi import FastAPI
from src.routes import routes
import uvicorn

app = FastAPI(
    version="0.0.1",
    title="API Friends",
    description="Esta é uma APi que irá retornar algumas características dos personagens da série Friends e também uma frase marcante de cada um"
)
app.include_router(routes, prefix="/friends")


if __name__ == "__main__":
    uvicorn.run(app)
