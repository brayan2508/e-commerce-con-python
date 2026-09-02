from fastapi import FastAPI
from app.db.session import create_db_and_tables
app = FastAPI(
    title="API Comercio y gestion de ordenes",
    version="1.0.0",
    description="API REST construida con FastAPI, SQLModel y Alembic"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables


@app.get("/")
def read_root():
    return {"status": "ok", "message": "*API de comercio activva y lista"}