from fastapi import APIRouter

from api.api_v1.horoskop import horoskop_anielski

horoskop_router = APIRouter()
horoskop_router.include_router(horoskop_anielski.router, prefix="/horoskop-anielski")
