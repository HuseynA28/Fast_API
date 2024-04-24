from fastapi import FastAPI
from fast_app.models import Customer
from database import create_db_and_tables, engine

app = FastAPI()

# Creates all tables
create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/customers/{id}")
async def get_customer(id: int):
    return {"data": f"Customer id : {id}"}


from sqlmodel import Session

@app.post("/customers")
async def create_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        return {"data": f"Customer {customer.CustomerID} is created."}
