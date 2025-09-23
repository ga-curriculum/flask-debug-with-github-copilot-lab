import pytest
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, users_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Bug: Not clearing global state between tests
        yield client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    # This will fail due to inconsistent response format
    assert data['status'] == 'healthy'
    assert 'message' in data

def test_get_data(client):
    """Test the data endpoint"""
    response = client.get('/api/data')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'users' in data
    # This will fail due to inconsistent key name
    assert 'total_count' in data
    assert len(data['users']) == 3

def test_get_user(client):
    """Test getting a single user"""
    # First populate data
    client.get('/api/data')
    
    response = client.get('/api/user/1')
    # This will fail due to type mismatch (string vs int)
    assert response.status_code == 200

def test_get_nonexistent_user(client):
    """Test getting a user that doesn't exist"""
    response = client.get('/api/user/999')
    # This will fail - should return 404, not 200
    assert response.status_code == 404

def test_create_user(client):
    """Test creating a new user"""
    user_data = {
        'name': 'David',
        'email': 'david@example.com'
    }
    response = client.post('/api/user', 
                          data=json.dumps(user_data),
                          content_type='application/json')
    assert response.status_code == 201  # This will fail - returns 200
    data = json.loads(response.data)
    assert data['name'] == 'David'
    assert data['email'] == 'david@example.com'

def test_create_user_invalid_data(client):
    """Test creating user with invalid data"""
    # This will cause a KeyError due to missing validation
    response = client.post('/api/user', 
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 400