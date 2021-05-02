
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_length_of_string():
    response = client.get('/strings/length?item=kavinder')
    assert response.status_code == 200
    assert response.json() == {"status_code": 200, "result": 8}


def test_generate_string():
    response = client.get('/strings/generate?num=10&item=k')
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"status_code": 200, "result": "kkkkkkkkkk"}
