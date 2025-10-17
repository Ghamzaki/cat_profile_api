# Cat Profile API

A simple FastAPI project that exposes a `/me` endpoint returning your profile info and a dynamic cat fact.

## Features
- Returns profile info (email, name, stack)
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

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set environment variables
Create a `.env` file in the project root (optional):
```
USER_EMAIL=your@email.com
USER_NAME=Your Name
USER_STACK=Python/FastAPI
```

### 5. Run the server
```
uvicorn main:app --reload
```

### 6. Test the endpoint
Visit: [http://localhost:8000/me](http://localhost:8000/me)

## Dependencies
- fastapi
- httpx
- python-dotenv
- uvicorn

## Notes
- If the Cat Facts API is down, a fallback message is returned.
- CORS is enabled for all origins by default.

## Author
- Name: Usman Ghamzaki Abdulhamid
- Email: uthmanghamzaki@gmail.com
- Stack: Python/FastAPI
