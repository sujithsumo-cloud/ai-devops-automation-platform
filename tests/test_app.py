
from app.main import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == "Application is running"
    assert data["environment"] == "BLUE"
    assert data["version"] == "v1"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["environment"] == "BLUE"
    assert data["version"] == "v1"
