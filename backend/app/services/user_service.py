from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin


def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, user: UserLogin):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return None

    if existing_user.password != user.password:
        return None

    return existing_user