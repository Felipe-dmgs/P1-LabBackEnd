from fastapi import FastAPI
from routers.tab_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Sistema para comandas de restaurante com MongoDB e FastAPI"}