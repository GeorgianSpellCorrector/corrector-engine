from typing import Union
from fastapi import FastAPI
from config import FastAPISettings
from starlette.middleware.cors import CORSMiddleware
from routers import api
from routers.utils import CorrectorRequest


settings = FastAPISettings()
app = FastAPI(**settings.model_dump())

app.include_router(api, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
