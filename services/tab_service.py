from repositories.tab_repository import *
from bson import ObjectId

def format_tab(tab):
    tab["_id"] = str(tab["_id"])
    return tab

def create_tab_service(tab):
    result = create_tab(tab.model_dump())
    return {"message": "Tab Created", "id": str(result.inserted_id)}

def get_all_tabs_service():
    tabs = get_all_tabs()
    return [format_tab(tab) for tab in tabs]

def get_tab_by_id_service(tab_id):
    try:
        tab = get_tab_by_id(tab_id)
    except:
        return {"error": "Invalid ID"}
    if not tab:
        return {"error": "Tab not found"}
    return format_tab(tab)

def update_tab_service(tab_id, tab):
    try:
        result = update_tab(tab_id, tab.model_dump())
    except:
        return {"error": "Invalid ID"}
    if result.matched_count == 0:
        return {"error": "Tab not found"}
    return {"message": "Tab Updated"}


def delete_tab_service(tab_id):
    try:
        result = delete_tab(tab_id)
    except:
        return {"error": "Invalid ID"}
    if result.deleted_count == 0:
        return {"error": "Tab not found"}
    return {"message": "Tab deleted"}
