from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL (SQLite database stored in the current directory)
DATABASE_URL = "sqlite:///./tasks.db"

# Create SQLAlchemy engine instance
# connect_args={"check_same_thread": False} is required only for SQLite in multi-threaded apps like FastAPI
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory for creating database sessions
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base class for SQLAlchemy ORM models
Base = declarative_base()


# Dependency function to provide a database session per request
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()