from fastapi import FastAPI
from app.schemas import EmailRequest,EmailResponse,AiRequest,AiResponse,SummaryRequest,SummaryResponse
from app.predictor import predict_email
from app.groq_ai import summarize_text, generate_ai_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "Spam Detection API")

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

@app.post("/summary",response_model = SummaryResponse)
def summary(data : SummaryRequest):
  try:
    summary_text = summarize_text(data.text)
    return SummaryResponse(text=summary_text)
  except Exception as e:
    return SummaryResponse(text=f"Error: {str(e)}")

@app.post("/ai-response",response_model = AiResponse)
def ai_response(data : AiRequest):
  try:
    response_text = generate_ai_response(data.text)
    return AiResponse(text=response_text)
  except Exception as e:
    return AiResponse(text=f"Error: {str(e)}")