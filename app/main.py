from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "iris_model.pkl")

# Load Model
model = joblib.load(model_path)

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def root():
    return {"message": "Welcome to the Iris Predictor API"}

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    pred = model.predict(features)[0]
    return {"prediction": int(pred)}