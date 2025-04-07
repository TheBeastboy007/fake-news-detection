from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class NewsRequest(BaseModel):
    title: str
    text: str

@app.get("/")
def home():
    return {"message": "Gateway running"}

@app.post("/predict")
def gateway_predict(news: NewsRequest):
    try:
        # Forward to AI model
        response = requests.post("http://ai-model:8000/predict", json=news.model_dump())
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling AI model: {e}")

@app.post("/submit-news")
def submit_news(news: NewsRequest):
    try:
        # Forward news sample to data-collection service
        response = requests.post("http://data-collection:5000/store", json=news.model_dump())
        return {"message": "News submitted", "details": response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
