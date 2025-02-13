import pytest
from data_generation.app import app


class TestDataGeneration:
    @pytest.fixture
    def client(self):
        with app.test_client() as client:
            yield client

    def test_valid_payload(self, client):
        payload = {"number_test_records": 100, "payload_key": "inputRecords"}
        response = client.post("/data_generation/v1/generate", json=payload)
        assert response.status_code == 201
