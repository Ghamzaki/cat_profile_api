# Cat Profile API

A simple FastAPI project that exposes a `/me` endpoint returning my profile info and a dynamic cat fact.

## Features
- Returns my profile info (email, name, stack)
- Fetches a random cat fact from https://catfact.ninja/fact
- Returns current UTC timestamp in ISO 8601 format
- Handles API errors gracefully
- CORS enabled
- Basic logging

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd cat_profile_api
```

### 2. Create and activate a virtual environment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Dependencies
- fastapi
- httpx
- python-dotenv
- uvicorn

## Install dependencies
```
- create a file "requirements.txt"
- pip install -r requirements.txt
```

### 4. Set environment variables
Create a `.env` file in the project root (optional):
```
USER_EMAIL=your@email.com
USER_NAME=Your Name
USER_STACK=Python/FastAPI
```

### 5. Run the server locally
```
uvicorn main:app --reload
```

### 6. Test the endpoint
Visit: [http://localhost:8000/me](http://localhost:8000/me)



## Deployment (Railway)

This API is deployed on Railway.
Live endpoint: https://catprofileapi-production.up.railway.app/me

### How to deploy on Railway:
1. Fork or clone this repo.
2. Sign up at https://railway.app/ and create a new project from your repo.
3. Set the start command: `uvicorn main:app --host=0.0.0.0 --port=8000`
4. Add environment variables in the Railway dashboard.
5. Deploy and get your public URL!

## Notes
- If the Cat Facts API is down, a fallback message is returned.
- CORS is enabled for all origins by default.

## Author
- Name: Usman Ghamzaki Abdulhamid
- Email: uthmanghamzaki@gmail.com
- Stack: Python/FastAPI
