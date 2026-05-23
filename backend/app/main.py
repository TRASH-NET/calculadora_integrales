from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.integration import router as integration_router

app = FastAPI()
app.include_router(integration_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "HOLA DANIELA"}
