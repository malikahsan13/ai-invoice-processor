from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.get_env("OPENAI_API_KEY"))


def extract_invoice_data(text: str) -> dict:
    prompt = f"""
        Extract invoice details from the following text.

    Return ONLY valid JSON with:
    vendor_name, invoice_number, amount, due_date

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a precise data extraction assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": "Invalid JSON from AI", "raw": content}
