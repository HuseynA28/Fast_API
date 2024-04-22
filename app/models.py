from sqlmodel import SQLModel, Field
from typing import Optional


class Customer(SQLModel, table=True):
    CustomerID: Optional[int] = Field(default=None, primary_key=True)
    customerFName: str
    customerLName: str
    customerEmail: str
    customerPassword: Optional[int]
    customerStreet: str
    customerCity: str