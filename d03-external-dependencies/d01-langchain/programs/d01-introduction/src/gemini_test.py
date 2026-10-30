import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Sending raw request...")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Why do parrots talk?",
)
print("Response received:")
print(response.text)
