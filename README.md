# Todo API

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
└── requirements.txt     # Project dependencies
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todo
```

2. Create and activate a virtual environment:
```bash
python -m venv fastapienv
source fastapienv/bin/activate  # On Windows: fastapienv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
alembic upgrade head
```

5. Start the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Testing

Run the test suite using pytest:
```bash
pytest
```

## Database

The application uses SQLite as the database. The database file is automatically created when you run the migrations.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 