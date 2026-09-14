from fastapi import FastAPI
from database import Base, engine
from routers import auth_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Internship & Job Application Tracker")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "API is running"}