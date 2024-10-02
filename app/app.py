from fastapi import FastAPI
from pydantic import BaseModel 
from model.model import predict_pipeline 
from model.model import __version__ as model_version 


app = FastAPI()

# === Create Schema === # 
class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str


@app.get("/")
async def root(): 
    return {"health_check": "OK", "API version": "0.1.0", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut) 
async def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

