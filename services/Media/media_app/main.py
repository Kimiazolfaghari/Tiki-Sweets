from fastapi import FastAPI
from media_app.api import media_routes

app = FastAPI()


app.include_router(media_routes.router, prefix="/media", tags=["Media"])
