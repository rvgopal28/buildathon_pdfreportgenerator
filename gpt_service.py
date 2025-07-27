from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # This will load variables from .env file


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert document drafter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
