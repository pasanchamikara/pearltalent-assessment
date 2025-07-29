from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_salesforce_integration():
    response = client.post(
        "/integrate/salesforce",
        json={"action": "create_lead", "parameters": {"name": "John"}},
        auth=("user", "pass")
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"