
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.api.user import router as user_router
from app.api.registration import router as registration_router
from app.api.event import router as event_router
from app.api.ticket import router as ticket_router
from app.api.payment import router as payment_router

from app.models.user import User
from app.models.event import Event
from app.models.ticket import Ticket
from app.models.registration import Registration
from app.models.payment import Payment

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
app.include_router(registration_router)
app.include_router(event_router)
app.include_router(ticket_router)
app.include_router(payment_router)


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
        "message": "API is healthy"
    }
