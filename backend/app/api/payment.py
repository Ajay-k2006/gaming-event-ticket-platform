from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.payment import Payment
from app.models.registration import Registration

router = APIRouter(prefix="/api/payments", tags=["Payments"])

@router.post("/")
def create_payment(registration_id: int, amount: float, payment_method: str, db: Session = Depends(get_db)):
    registration = db.query(Registration).filter(Registration.id == registration_id).first()
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    payment = Payment(registration_id=registration_id, amount=amount, payment_method=payment_method, payment_status="pending")
    db.add(payment)
    db.commit()
    db.refresh(payment)

    return {
        "success": True,
        "message": "Payment created successfully",
        "payment": {
            "id": payment.id,
            "registration_id": payment.registration_id,
            "amount": payment.amount,
            "payment_method": payment.payment_method,
            "payment_status": payment.payment_status
        }
    }

@router.get("/")
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()

@router.put("/{payment_id}")
def update_payment(payment_id: int, payment_status: str, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    if payment_status not in ["pending", "completed", "failed"]:
        raise HTTPException(status_code=400, detail="Invalid payment status")

    payment.payment_status = payment_status
    db.commit()
    db.refresh(payment)

    return {
        "success": True,
        "message": "Payment status updated successfully",
        "payment": {
            "id": payment.id,
            "registration_id": payment.registration_id,
            "amount": payment.amount,
            "payment_method": payment.payment_method,
            "payment_status": payment.payment_status
        }
    }