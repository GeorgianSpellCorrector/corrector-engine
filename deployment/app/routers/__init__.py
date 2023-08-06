from fastapi import APIRouter
from routers import inference

api = APIRouter()

api.include_router(inference.router, prefix="/inference", tags=["inference"])
