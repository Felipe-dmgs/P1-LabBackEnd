from fastapi import APIRouter
from schemas.tab_schema import Tab
from services.tab_service import *

router = APIRouter()


@router.get("/tabs")
def list_tabs():
    return get_all_tabs_service()


@router.post("/tabs")
def create_tab(tab: Tab):
    return create_tab_service(tab)


@router.get("/tabs/{tab_id}")
def get_tab(tab_id: str):
    return get_tab_by_id_service(tab_id)


@router.put("/tabs/{tab_id}")
def update_tab(tab_id: str, tab: Tab):
    return update_tab_service(tab_id, tab)


@router.delete("/tabs/{tab_id}")
def delete_tab(tab_id: str):
    return delete_tab_service(tab_id)