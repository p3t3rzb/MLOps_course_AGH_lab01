import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import joblib
from cleantext import clean
from sentence_transformers import SentenceTransformer

MODEL_DIR = Path(os.getenv("MODEL_DIR", "model"))
LABELS = {0: "negative", 1: "neutral", 2: "positive"}


@dataclass(frozen=True)
class SentimentModel:
    encoder: SentenceTransformer
    classifier: Any


@lru_cache(maxsize=1)
def load_model(model_dir: Path = MODEL_DIR) -> SentimentModel:
    encoder = SentenceTransformer(
        str(model_dir / "sentence_transformer.model"), device="cpu"
    )
    classifier = joblib.load(model_dir / "classifier.joblib")
    return SentimentModel(encoder=encoder, classifier=classifier)


def preprocess(text: str) -> str:
    return str(clean(text, lower=True, no_line_breaks=True))


def predict(model: SentimentModel, text: str) -> str:
    embedding = model.encoder.encode([preprocess(text)])
    class_index = int(model.classifier.predict(embedding)[0])
    return LABELS[class_index]
