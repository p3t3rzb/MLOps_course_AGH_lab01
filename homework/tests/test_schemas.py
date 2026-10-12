import pytest
from pydantic import ValidationError

from api.schemas import PredictRequest, PredictResponse


def test_valid_request() -> None:
    assert PredictRequest(text="Nice lecture").text == "Nice lecture"


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_empty_text_rejected(text: str) -> None:
    with pytest.raises(ValidationError):
        PredictRequest(text=text)


@pytest.mark.parametrize("text", [None, 123, ["a"]])
def test_non_string_text_rejected(text: object) -> None:
    with pytest.raises(ValidationError):
        PredictRequest.model_validate({"text": text})


def test_response_serialization() -> None:
    assert PredictResponse(prediction="positive").model_dump() == {
        "prediction": "positive"
    }
