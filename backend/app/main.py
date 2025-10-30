from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.identify import router as identify_router

app = FastAPI(
    title="WhatBird Backend API",
    description="Identify birds from recorded audio using an ML model",
    version="1.0.0"
)

# Allow frontend or other clients to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(identify_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "WhatBird API running successfully!"}
