from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.integration import router as integration_router
import os

app = FastAPI()
app.include_router(integration_router)
origins = os.getenv("ALLOWED_ORIGINS", "").split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST, GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "HOLA DANIELA"}
