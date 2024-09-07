from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this for your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routers
from .routes import auth, campaign, army_builder, forum, profile

app.include_router(auth.router)
app.include_router(campaign.router)
app.include_router(army_builder.router)
app.include_router(forum.router)
app.include_router(profile.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Warhammer App API"}
