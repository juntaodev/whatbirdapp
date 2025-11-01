# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.identify import router as identify_router

app = FastAPI(title="WhatBirdApp API", version="0.1.0")

# CORS for local dev (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

app.include_router(identify_router)
