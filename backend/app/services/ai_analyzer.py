from ..core.config import settings
from google.genai import types
from google import genai
from fastapi import HTTPException
from pydantic import BaseModel
import asyncio
api_key = settings.gemini_api_key
client = genai.Client(api_key=api_key)

class PromptRequest(BaseModel):
    prompt: str

async def generate_text(request: PromptRequest):
    try:
        # Call the Gemini model (using a free tier model like gemini-2.5-flash or gemini-2.0-flash)
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=request.prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
            ),
        )
        return {"response": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
async def test_generate_text():
    response = await generate_text(PromptRequest(prompt="Hello, how are you?"))
    print(response)

asyncio.run(test_generate_text())