import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv("../.env")  # load API_KEY, OPENAI_API_KEY, etc.

app = FastAPI(title="My Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock down to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routes import dummy
app.include_router(dummy.router, prefix="/api")
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("/health")

async def health():

    return {"status": "healthy"}

@app.get("/env")

async def env():
    env_vars = {
        "API_KEY": os.getenv("API_KEY"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
    return env_vars
@app.get("/api-key")
async def api_key():
    api_key = os.getenv("API_KEY")
    if api_key:
        return {"api_key": api_key}
    else:
        return {"error": "API_KEY not found in environment variables."}
@app.get("/openai-api-key")
async def openai_api_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        return {"openai_api_key": openai_api_key}
    else:
        return {"error": "OPENAI_API_KEY not found in environment variables."}
@app.get("/api-key")
async def api_key():
    api_key = os.getenv("API_KEY")
    if api_key:
        return {"api_key": api_key}
    else:
        return {"error": "API_KEY not found in environment variables."}