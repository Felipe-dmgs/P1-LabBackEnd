from pydantic import BaseModel

class Tab(BaseModel):
    TableNumber: int
    Price: float
    Waiter: str
    People: int
    Orders: list
