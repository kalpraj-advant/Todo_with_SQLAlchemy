## Todo APP

- User authentication and authorization
- CRUD operations for todo items
- SQLAlchemy ORM for database operations
- Alembic for database migrations
- Pytest for testing
- FastAPI automatic API documentation

## Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Pytest


## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/kalpraj-advant/Todo_with_SQLAlchemy
cd Todo_with_SQLAlchemy
```

2. Install dependencies using uv:
```bash
uv pip install -e .
```

3. Run database migrations:
```bash
alembic upgrade head
```

4. Start the application:
```bash
uv run uvicorn app.main:app --reload
```
5. Testing : Run the test suite using pytest:
```bash
uv run pytest
or
pytest tests/ -v
```

The API will be available at `http://127.0.0.1:8000`

## API Documentation

Once the application is running, you can access:
- UI documentation: `http://127.0.0.1:8000/docs`


## Project Structure

```
.
├── alembic/              # Database migration files
├── app/
│   ├── api/             # API endpoints
│   ├── config/          # Configuration files
│   ├── core/            # Core functionality
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   └── services/        # Business logic
├── tests/               # Test files
├── alembic.ini          # Alembic configuration
├── main.py             # Application entry point
└── pyproject.toml      # Project dependencies
```