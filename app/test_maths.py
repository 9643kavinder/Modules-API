
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_fibonacci():
    response = client.get('/maths/fibonacci?num=3')
    assert response.status_code == 200
    assert response.json() == {"status_code": 200, "result": 1}


def test_factorial():
    response = client.get('/maths/factorial?num=4')
    assert response.status_code == 200
    assert response.json() == {"status_code": 200, "result": 24}
