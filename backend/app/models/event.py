from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    event_date = Column(DateTime, nullable=False)
    venue = Column(String, nullable=False)

    organizer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )