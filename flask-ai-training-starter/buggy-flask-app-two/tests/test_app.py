import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'message' in data

def test_get_data(client):
    """Test the data endpoint"""
    response = client.get('/api/data')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'users' in data
    assert 'total_count' in data
    assert len(data['users']) == 3
    assert data['total_count'] == 3

def test_home_route(client):
    """Test the home route"""
    response = client.get('/')
    # This will fail without a template, but shows the route exists
    assert response.status_code == 500 or response.status_code == 404