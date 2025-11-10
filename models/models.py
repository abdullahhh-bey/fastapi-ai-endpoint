from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt : str = Field(...)
    
class ChatRespone(BaseModel):
    answer : str
    