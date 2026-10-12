from fastapi import FastAPI

from api.schemas import PredictRequest, PredictResponse
from inference import load_model, predict as predict_sentiment

app = FastAPI(title="Sentiment Analysis API")
model = load_model()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction=predict_sentiment(model, request.text))
