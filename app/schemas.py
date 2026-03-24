from pydantic import BaseModel

class EmailRequest(BaseModel):
  text : str

class EmailResponse(BaseModel):
  prediction : str
  confidence : float
  spam_probability : float
  ham_probability : float

class SummaryRequest(BaseModel):
  text : str

class SummaryResponse(BaseModel):
  text : str

class AiRequest(BaseModel):
  text : str

class AiResponse(BaseModel):
  text : str