from fastapi import FastAPI, HTTPException
from models.models import ChatRequest, ChatRespone
from ai.gemini import GeminiService
from ssecrets import GEMINI_KEY
from middleware.rateLimitingMiddleware import RateLimitingMiddleware

app = FastAPI()

gemini = GeminiService(api_key=GEMINI_KEY)

app.add_middleware(RateLimitingMiddleware)

@app.post("/ask", response_model=ChatRespone)
async def generate_content(req: ChatRequest):
    try:
        result = gemini.generate(req.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
