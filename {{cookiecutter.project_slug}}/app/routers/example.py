from lib2to3.pytree import Base
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Greeting(BaseModel):
    greeting:str 

@router.get("/say_hello", response_model=Greeting, tags=["Hello, World"])
async def say_hello():
    return {
        "greeting": "Hello, {{cookiecutter.author}}"
    }
