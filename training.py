import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.utils import Bunch

MODEL_PATH = "model.joblib"


def load_data() -> Bunch:
    return load_iris()


def train_model(data: Bunch) -> LogisticRegression:
    model = LogisticRegression(max_iter=1000)
    model.fit(data.data, data.target)
    return model


def save_model(model: LogisticRegression, path: str = MODEL_PATH) -> None:
    joblib.dump(model, path)


if __name__ == "__main__":
    save_model(train_model(load_data()))
