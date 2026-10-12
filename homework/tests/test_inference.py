import pytest

from inference import LABELS, SentimentModel, load_model, predict


@pytest.fixture(scope="module")
def model() -> SentimentModel:
    return load_model()


def test_model_loads(model: SentimentModel) -> None:
    assert model.encoder.get_embedding_dimension() == 384
    assert list(model.classifier.classes_) == [0, 1, 2]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("What a great MLOps lecture, I am very satisfied", "positive"),
        ("This is terrible, I hate it", "negative"),
        ("The lecture is on Tuesday.", "neutral"),
    ],
)
def test_predict_sample_texts(model: SentimentModel, text: str, expected: str) -> None:
    prediction = predict(model, text)
    assert prediction in LABELS.values()
    assert prediction == expected
