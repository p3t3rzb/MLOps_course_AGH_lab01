from fastapi import FastAPI

from api.schemas import PredictRequest, PredictResponse

app = FastAPI(title="Sentiment Analysis API")


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction="positive")
