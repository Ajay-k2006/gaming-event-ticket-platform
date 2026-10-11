from pydantic import BaseModel
from datetime import datetime


class EventCreate(BaseModel):
    title: str
    description: str
    event_date: datetime
    venue: str
    organizer_id: int


class EventUpdate(BaseModel):
    title: str
    description: str
    event_date: datetime
    venue: str


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    event_date: datetime
    venue: str
    organizer_id: int

    class Config:
        from_attributes = True