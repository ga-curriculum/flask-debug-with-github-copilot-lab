# Flask AI Training - Starter

This is the starter version of a Flask application for AI training purposes.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pipenv install -r requirements.txt
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Run the application:
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