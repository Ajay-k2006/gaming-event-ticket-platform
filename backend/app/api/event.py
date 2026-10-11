from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.event import Event
from app.schemas.event_schema import EventCreate, EventUpdate

router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)


@router.post("/")
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):
    new_event = Event(
        title=event.title,
        description=event.description,
        event_date=event.event_date,
        venue=event.venue,
        organizer_id=event.organizer_id
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "success": True,
        "message": "Event created successfully",
        "event": {
            "id": new_event.id,
            "title": new_event.title,
            "description": new_event.description,
            "event_date": new_event.event_date,
            "venue": new_event.venue,
            "organizer_id": new_event.organizer_id
        }
    }


@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()


@router.get("/{event_id}")
def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


@router.put("/{event_id}")
def update_event(
    event_id: int,
    event: EventUpdate,
    db: Session = Depends(get_db)
):
    existing_event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not existing_event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    existing_event.title = event.title
    existing_event.description = event.description
    existing_event.event_date = event.event_date
    existing_event.venue = event.venue

    db.commit()
    db.refresh(existing_event)

    return {
        "success": True,
        "message": "Event updated successfully",
        "event": existing_event
    }


@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    db.delete(event)
    db.commit()

    return {
        "success": True,
        "message": "Event deleted successfully"
    }