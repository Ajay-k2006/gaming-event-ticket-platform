from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.registration import Registration
from app.models.user import User
from app.models.ticket import Ticket


router = APIRouter(
    prefix="/api/registrations",
    tags=["Registrations"]
)


@router.post("/")
def create_registration(
    user_id: int,
    ticket_id: int,
    quantity: int = 1,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    if quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )

    if quantity > ticket.quantity:
        raise HTTPException(
            status_code=400,
            detail="Not enough tickets available"
        )

    registration = Registration(
        user_id=user_id,
        ticket_id=ticket_id,
        quantity=quantity
    )

    ticket.quantity = ticket.quantity - quantity

    db.add(registration)
    db.commit()
    db.refresh(registration)

    return {
        "success": True,
        "message": "Registration successful",
        "registration": {
            "id": registration.id,
            "user_id": registration.user_id,
            "ticket_id": registration.ticket_id,
            "quantity": registration.quantity
        }
    }

@router.get("/")
def get_registrations(db: Session = Depends(get_db)):
    registrations = db.query(Registration).all()

    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "ticket_id": r.ticket_id,
            "quantity": r.quantity
        }
        for r in registrations
    ]
