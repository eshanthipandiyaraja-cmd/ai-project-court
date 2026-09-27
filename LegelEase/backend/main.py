from fastapi import FastAPI
from backend.routes import router

app = FastAPI()

app.include_router(router)
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "LegalEase Backend Active"}