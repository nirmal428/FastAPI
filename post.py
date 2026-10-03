from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class users(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:users):
    return{
        "mesasage":"User Created",
        "data":user
    }