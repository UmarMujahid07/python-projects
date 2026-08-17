from sqlalchemy import Boolean, Column, Integer, String
from database import Base


# SQLAlchemy Database Model for Tasks table
class TaskDB(Base):
    __tablename__ = "tasks"

    # Primary key column with auto-incrementing integer ID
    id = Column(Integer, primary_key=True, index=True)

    # Task details columns
    title = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    priority = Column(String, default="Medium")