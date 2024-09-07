from fastapi import FastAPI
from .routes import auth, campaign, army_builder, forum, profile
from .models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./warhammer_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(campaign.router)
app.include_router(army_builder.router)
app.include_router(forum.router)
app.include_router(profile.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Warhammer App API"}
