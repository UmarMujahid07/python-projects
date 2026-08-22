from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


# SQLAlchemy model representing registered application users
class UserDB(Base):
    __tablename__ = "users"

    # Unique user identifier
    id = Column(Integer, primary_key=True, index=True)

    # User credentials
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# SQLAlchemy model representing todo items linked to specific users
class TodoDB(Base):
    __tablename__ = "todos"

    # Primary key for todo records
    id = Column(Integer, primary_key=True, index=True)

    # Todo details
    title = Column(String)
    is_completed = Column(Boolean, default=False)

    # Foreign key referencing the primary key of the users table
    owner_id = Column(Integer, ForeignKey("users.id"))