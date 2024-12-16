'''
FastAPI App

terminal
run the command:
conda activate yourenvname
cd src
uvicorn app:app --reload

or 

uvicorn src.app:app --reload

open
http://127.0.0.1:8000/

open
http://127.0.0.1:8000/docs


To get the prediction for the post sideway 5 bar change:
open another terminal

then run the curl command
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "num_candles": 0,
  "price_range_pct": 0,
  "num_res_hits": 0,
  "num_sup_hits": 0,
  "num_res_breakouts": 0,
  "num_sup_breakouts": 0,
  "alternation": 0,
  "last_candle_return": 0,
  "last_candle_pct_above_support": 0,
  "concentration_score_scaled": 0,
  "alternation_score_scaled": 0,
  "pre_sideway_5_bar_change": 0,
  "pre_sideway_10_bar_change": 0
}'
'''


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create the FastAPI app
app = FastAPI()

# Load the saved model from weights folder
model = joblib.load("../weights/best_rf_model.pkl")

# Define the input data structure
class InputData(BaseModel):
    num_candles: float
    price_range_pct: float
    num_res_hits: float
    num_sup_hits: float
    num_res_breakouts: float
    num_sup_breakouts: int
    alternation: float
    last_candle_return: float
    last_candle_pct_above_support: float
    concentration_score_scaled: float
    alternation_score_scaled: float
    pre_sideway_5_bar_change: float
    pre_sideway_10_bar_change: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the QuantForecaster API"}

# Prediction endpoint
@app.post("/predict/")
def predict(data: InputData):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    prediction = model.predict(input_df)

    # Return prediction
    return {"prediction": prediction[0]}