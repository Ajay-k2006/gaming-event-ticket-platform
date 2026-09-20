from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.api.user import router as user_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gaming Event Ticket Platform",
    description="Backend API for the Gaming Event Ticket Platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "Gaming Event Ticket Platform API is running"
    }


@app.get("/api/health")
def health():
    return {
        "success": True,
        "message": "Backend is healthy"
    }