from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.ticket import Ticket
from app.models.event import Event

router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"]
)


@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()


@router.get("/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@router.post("/")
def create_ticket(
    event_id: int,
    ticket_type: str,
    price: float,
    quantity: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if price < 0 or quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Price and quantity cannot be negative"
        )

    ticket = Ticket(
        event_id=event_id,
        ticket_type=ticket_type,
        price=price,
        quantity=quantity
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {
        "success": True,
        "message": "Ticket created successfully",
        "ticket": {
            "id": ticket.id,
            "event_id": ticket.event_id,
            "ticket_type": ticket.ticket_type,
            "price": ticket.price,
            "quantity": ticket.quantity
        }
    }


@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket_type: str,
    price: float,
    quantity: int,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if price < 0 or quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Price and quantity cannot be negative"
        )

    ticket.ticket_type = ticket_type
    ticket.price = price
    ticket.quantity = quantity

    db.commit()
    db.refresh(ticket)

    return {
        "success": True,
        "message": "Ticket updated successfully",
        "ticket": {
            "id": ticket.id,
            "event_id": ticket.event_id,
            "ticket_type": ticket.ticket_type,
            "price": ticket.price,
            "quantity": ticket.quantity
        }
    }


@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    db.delete(ticket)
    db.commit()

    return {
        "success": True,
        "message": "Ticket deleted successfully"
    }
