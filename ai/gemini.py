from google import genai
from .base import AIPlatform
from models.models import ChatRespone

class GeminiService:
    def __init__(self, api_key: str, default_model: str = "gemini-2.5-flash"):
        self.client = genai.Client(api_key=api_key)
        self.system_prompt = "Always give response plain text. Use simple, logical, clear approach to give your answer"
        self.default_model = default_model

    def generate(self, prompt: str) -> str:
        model = self.default_model
        UserPrompt = f"{self.system_prompt}\n\n{prompt}"
        
        response = self.client.models.generate_content(
            model=model,
            contents=UserPrompt
        )
        
        res = ChatRespone(
            answer = response.text
        )
        return res
