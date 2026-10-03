from fastapi import FastAPI , Path , HTTPException ,Query
import json

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


@app.get("/about")
def about():
    return {
        "message": "A Fully Functional API to Manage Your Patient Records"
    }


@app.get("/view")
def view():
    data = load_data()

    return data

@app.get('/patient/{id}')
def view_patient(id:int):
    #load all the patient
    data=load_data()

    for patient in data:
        if patient["id"] == id:
            return patient
    raise HTTPException(status_code=404, detail="Patient Not Found ")


@app.get('/sort')
def sort_patient(sort_by:str = Query(... , description="sort on the bases of age "), order: str = Query("asc",description="sort in asc or desc order")):
    valid_field = ['age']
    if sort_by not in valid_field:
        raise HTTPException(status_code=400 , detail="Invailed field")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="invailid order select")

    data = load_data()