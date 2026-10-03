from fastapi import FastAPI

app = FastAPI()



#about routes
@app.get("/user/{user_id}")
def get_user(user_id):
    return{"user_id":user_id}