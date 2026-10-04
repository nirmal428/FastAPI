from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos =[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/totos")
def create_todo(todo:Todo):
    todos.append(todo)    
    return {"meassage":"Todo added ","Data":todo}

@app.get("/todos")
def get_todos():
    return todos