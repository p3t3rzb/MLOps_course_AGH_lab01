import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_predict_returns_valid_json() -> None:
    response = client.post(
        "/predict", json={"text": "What a great MLOps lecture, I am very satisfied"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"prediction": "positive"}


@pytest.mark.parametrize("payload", [{"text": ""}, {"text": 5}, {}, {"txt": "hi"}])
def test_invalid_input_returns_error_json(payload: dict[str, object]) -> None:
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert body["detail"]
    assert all("msg" in error and "loc" in error for error in body["detail"])
