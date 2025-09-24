# Bonus Buggy Flask App Starter

This is the starter version of a Flask application for AI training purposes.

## Setup

Install dependencies:

```bash
pipenv install -r requirements.txt
```

Activate the virtual environment:

```bash
pipenv shell
```

Run the application:
   
```bash
python app.py
```

  or 

```bash
pipenv run python app.py
```

## API Endpoints

- `GET /` - Home page (requires template)
- `GET /api/health` - Health check endpoint
- `GET /api/data` - Returns sample user data

## Testing

Run tests with:
```bash
pytest tests/
```

## Features

This starter application includes:
- Basic Flask setup
- JSON API endpoints
- Health check endpoint
- Sample data endpoint
- Basic test structure