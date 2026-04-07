from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["P2BackEnd"]

tab_collection = db["Tabs"]