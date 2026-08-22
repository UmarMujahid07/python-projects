# importing dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL for SQLite
DATABASE_URL = "sqlite:///./todo_app.db"

# Engine configuration with multi-threading support for SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Database session factory
LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Declarative base class for ORM models
Base = declarative_base()


# Dependency to yield database sessions per request lifecycle
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()