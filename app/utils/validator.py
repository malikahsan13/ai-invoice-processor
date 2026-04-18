from datetime import datetime

REQUIRED_FIELDS = ["vendor_name", "invoice_number", "amount", "due_date"]


def validate_invoice_data(data: dict):
    """
    Validate AI extracted invoice data.
    Returns: (in_valid): bool, error: str | None)
    """

    # Type check
    if not isinstance(data, dict):
        return False, "Invalid format: expected dictionary"

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f"Missing field: {field}"

        if data[field] in [None, "", []]:
            return False, f"Emoty field: {field}"

    # Validate amount
    try:
        amount = float(data["amount"])
        if amount <= 0:
            return False, "Amount must be greater than 0"
    except (ValueError, TypeError):
        return False, "Amount must be a number"

    # Validate date
    try:
        datetime.strptime(data["due_date"], "%Y-%m-%d")
    except ValueError:
        return False, "Invalid due_date format (expected YYYY-MM-DD)"

    return True, None


def normalize_invoice_data(data: dict) -> dict:
    return {
        "vendor_name": data["vendor_name"].strip(),
        "invoice_number": data["invoice_number"].strip(),
        "amount": float(data["amount"]),
        "due_date": data["due_date"]
    }
