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
