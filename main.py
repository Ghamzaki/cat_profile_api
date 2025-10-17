from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
import httpx
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import logging

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Enable CORS for all origins (customize as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAT_FACTS_URL = "https://catfact.ninja/fact"

@app.get("/me", response_class=JSONResponse)
async def get_profile():
    try:
        # Fetch cat fact dynamically
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CAT_FACTS_URL)
            response.raise_for_status()
            data = response.json()
            cat_fact = data.get("fact", "Cats are mysterious creatures!")
            logger.info("Fetched cat fact successfully.")
    except Exception as e:
        cat_fact = "Could not fetch a cat fact at the moment."
        logger.error(f"Error fetching cat fact: {e}")

    # Current UTC time in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat()

    payload = {
        "status": "success",
        "user": {
            "email": os.getenv("USER_EMAIL", "uthmanghamzaki@gmail.com"),
            "name": os.getenv("USER_NAME", "Usman Ghamzaki Abdulhamid"),
            "stack": os.getenv("USER_STACK", "Python/FastAPI")
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return JSONResponse(content=payload, media_type="application/json")