# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.api.v1 import auth, todos
# from app.core.database import engine, Base

# # Create database tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Include routers
# app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
# app.include_router(todos.router, prefix="/api/v1", tags=["todos"])

# @app.get("/")
# async def root():
#     return {"message": "Hello"}