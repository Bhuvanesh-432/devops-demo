import sys
import os

# Make sure Python can find app.py, which lives one directory above this test file.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app


@pytest.fixture
def client():
    """
    A pytest fixture: a reusable piece of setup that any test function can
    request just by naming it as an argument (see 'client' below).
    Flask's test_client() lets us simulate HTTP requests without running
    a real server.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_content(client):
    response = client.get("/")
    assert response.data.decode() == "Hello DevOps!"


def test_health_status_code(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_content(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "healthy"}
