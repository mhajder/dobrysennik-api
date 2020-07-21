from fastapi import APIRouter

from api.api_v1.horoskop.api import horoskop_router

api_v1_router = APIRouter()
api_v1_router.include_router(horoskop_router, prefix="/horoskop", tags=["Horoskop"])
