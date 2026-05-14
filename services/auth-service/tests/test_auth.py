from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_login_success():
    client = app.test_client()
    response = client.post("/login", json={
        "username": "admin",
        "password": "admin123"
    })

    assert response.status_code == 200
    assert response.get_json()["token"] == "fake-jwt-token"