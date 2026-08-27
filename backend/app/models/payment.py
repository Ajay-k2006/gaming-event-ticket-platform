from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    registration_id = Column(
        Integer,
        ForeignKey("registrations.id"),
        nullable=False
    )

    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    payment_status = Column(String, nullable=False, default="pending")