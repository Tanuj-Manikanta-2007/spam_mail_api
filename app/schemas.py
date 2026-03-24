from pydantic import BaseModel

class EmailRequest(BaseModel):
  text : str

class EmailResponse(BaseModel):
  prediction : str
  confidence : float
  spam_probability : float
  ham_probability : float