from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey
# from sqlalchemy.orm import declarative_base, sessionmaker
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get database URL from environment variable
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()

# class Todo(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     description = Column(String)
#     completed = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     username = Column(String, unique=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

# # Create tables
# Base.metadata.create_all(bind=engine)

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()