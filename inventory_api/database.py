import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use DATABASE_URL from environment if it exists, otherwise use SQLite
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./inventory.db")

# A small adjustment is needed for SQLite vs. PostgreSQL
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    # SQLite-specific configuration
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL configuration
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()