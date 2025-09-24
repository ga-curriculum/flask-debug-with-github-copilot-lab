# Buggy Flask App Starter

This is the buggy version of a Flask application for AI training purposes. This version contains intentional bugs and issues for debugging practice.

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
   
## Known Issues

This version contains several intentional bugs:

1. **Template Issues**: Missing template files
2. **Response Format Inconsistencies**: Mixed response formats
3. **Input Validation**: Missing validation for user inputs
4. **Error Handling**: Improper HTTP status codes
5. **Type Mismatches**: String/integer comparison issues
6. **Global State Management**: Poor handling of global variables
7. **Security Issues**: Debug mode enabled with public host
8. **Test Issues**: Failing tests due to various bugs

## API Endpoints

- `GET /` - Home page (will fail due to missing template)
- `GET /api/health` - Health check endpoint (inconsistent format)
- `GET /api/data` - Returns user data (inconsistent field names)
- `GET /api/user/<user_id>` - Get specific user (type validation issues)
- `POST /api/user` - Create new user (missing validation)

## Testing

Run tests to see failures:
```bash
pytest tests/ -v
```

Most tests will fail due to the intentional bugs.

## Exercise Goal

The goal is to identify and fix all the bugs to make this application work correctly and pass all tests.