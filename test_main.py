# test_main.py
import pytest
from main import app


@pytest.fixture
def client():
    """
    Pytest fixture that creates a Flask test client from the 'app' in main.py.
    """
    with app.test_client() as client:
        yield client


def test_root_endpoint(client):
    """
    Test the GET '/' endpoint to ensure it returns
    the greeting and a 200 status code.
    """
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from my Password Validator!" in resp.data


def test_check_password_accurate_password(client):
    """
    Test the POST '/v1/checkPassword' endpoint to ensure
    it returns true when password is valid
    """
    resp = client.post("/v1/checkPassword", json={"password": "Password1!"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("valid") is True