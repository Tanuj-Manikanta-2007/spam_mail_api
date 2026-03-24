from fastapi import FastAPI
from app.schemas import EmailRequest,EmailResponse
from app.predictor import predict_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(tilte = "Spam Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
  return {"message" : "Spam Detection API is running "}

@app.post("/predict",response_model=EmailResponse)
def predict(data : EmailRequest):
  result = predict_email(data.text)
  return result