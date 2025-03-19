import openai

def generate_ai_summary(page_data):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Summarize this page: {page_data}"}]
    )
    return response["choices"][0]["message"]["content"]
