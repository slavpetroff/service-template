# My Microservice

This is a microservice project generated using the Microservice Cookiecutter Template.

## Getting Started

To run the microservice, follow these steps:

1. Install dependencies:

```bash
poet install
```

2. Run the microservice:

```bash
uvicorn api.main:app --reload
```

3. Access the API at http://localhost:8000

## Database Migrations

To create and apply database migrations using Alembic:

- Create a new migration:
    
```bash
alembic revision --autogenerate -m "Add users table"
```

- Apply migrations:

```bash
alembic upgrade head
```

## Running Tests

To run tests for the microservice, use Pytest:

```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
