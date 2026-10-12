import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from training import MODEL_PATH

CLASS_NAMES = load_iris().target_names


def load_model(path: str = MODEL_PATH) -> LogisticRegression:
    return joblib.load(path)


def predict(model: LogisticRegression, features: list[float]) -> str:
    class_index = model.predict([features])[0]
    return str(CLASS_NAMES[class_index])
