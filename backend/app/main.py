from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import Base
from .db import engine
from .crud import list_reviews
from .twilio_webhook import router as whatsapp_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(whatsapp_router)

@app.get("/api/reviews")
async def get_reviews():
    return await list_reviews()
