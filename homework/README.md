# Sentiment analysis API

FastAPI server serving a Sentence Transformer + logistic regression sentiment model.

## Setup

Download the model from [Google Drive](https://drive.google.com/file/d/1NRZdYq5jweVRUzAZG518LMhs4E56IgxG/view) and unpack it into `model/`:

```
model/
├── classifier.joblib
└── sentence_transformer.model/
```

## Run

```bash
uv sync
uv run uvicorn app:app --port 8000   # locally
docker compose up                    # in Docker
uv run pytest                        # tests
```
