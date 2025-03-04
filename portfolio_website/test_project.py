import pytest
from project import app  # Import Flask app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True  #  testing mode
    with app.test_client() as client:
        yield client  #  test client

def test_home(client):
    """Test the home page."""
    response = client.get('/')  #  request to the home page
    assert response.status_code == 200  # Check that the response status code is 200
    assert b'Welcome to My Portfolio' in response.data  # Check for specific content

def test_about(client):
    """Test the about page."""
    response = client.get('/about')  
    assert response.status_code == 200  
    assert b'About Me' in response.data  

def test_contact(client):
    """Test the contact page."""
    response = client.get('/contact')  
    assert response.status_code == 200  
    assert b'Contact Me' in response.data  

def test_contact_form_submission(client):
    """Test the contact form submission."""
    response = client.post('/contact', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'This is a test message.'
    })
    assert response.status_code == 302  # check redirect after form submission
    assert response.location == 'http://localhost:5000/'  # Check that it redirects to the home page