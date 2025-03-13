import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_summary(page_data):
    prompt = f"Summarize the LinkedIn page insights:\n\n{page_data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
