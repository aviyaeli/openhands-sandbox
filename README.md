# FastAPI Boilerplate

A boilerplate FastAPI application with a structured project layout.

## Features

- Structured project layout
- CORS middleware enabled
- Example API endpoints for items
- Pydantic models for data validation
- Environment variable support

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   └── routers/
│       ├── __init__.py
│       └── items.py
├── .env
├── main.py
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository
2. Install uv (a faster Python package installer and resolver):

```bash
curl -sSf https://astral.sh/uv/install.sh | bash
```

3. Create and activate a virtual environment with uv:

```bash
uv venv
source .venv/bin/activate  # On Linux/macOS
# OR
.venv\Scripts\activate     # On Windows
```

4. Install dependencies using uv:

```bash
uv pip install -r requirements.txt
```

## Running the Application

Using uv:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 12000 --reload
```

Using uvicorn directly (after installing with uv):

```bash
uvicorn main:app --host 0.0.0.0 --port 12000 --reload
```

Or simply run with uv:

```bash
uv run python main.py
```

## API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: http://localhost:12000/docs
- ReDoc: http://localhost:12000/redoc

## API Endpoints

- `GET /`: Root endpoint with welcome message
- `GET /health`: Health check endpoint
- `GET /items/`: Get a list of items
- `GET /items/{item_id}`: Get a specific item
- `POST /items/`: Create a new item
- `PUT /items/{item_id}`: Update an existing item
- `DELETE /items/{item_id}`: Delete an item
