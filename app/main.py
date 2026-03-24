from fastapi import FastAPI
from app.schemas import EmailRequest,EmailResponse
from app.predictor import predict_email

app = FastAPI(tilte = "Spam Detection API")

@app.get("/")
def home():
  return {"message" : "Spam Detection API is running "}

@app.post("/predict",response_model=EmailResponse)
def predict(data : EmailRequest):
  result = predict_email(data.text)
  return result