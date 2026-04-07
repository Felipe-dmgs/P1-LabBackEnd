from database import tab_collection
from bson import ObjectId

def create_tab(tab_dict):
    return tab_collection.insert_one(tab_dict)

def get_all_tabs():
    return list(tab_collection.find())

def get_tab_by_id(tab_id):
    return tab_collection.find_one({"_id": ObjectId(tab_id)})

def update_tab(tab_id, tab_dict):
    return tab_collection.update_one(
        {"_id": ObjectId(tab_id)},
        {"$set": tab_dict}
    )

def delete_tab(tab_id):
    return tab_collection.delete_one(
        {"_id": ObjectId(tab_id)}
    )