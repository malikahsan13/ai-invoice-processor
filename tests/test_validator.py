from app.utils.validator import validate_invoice_data


def test_valid_data():
    data = {
        "vendor_name": "ABc",
        "invoice_number": "123",
        "amount": 100,
        "due_date": "2024=10-01"
    }

    is_valid, error = validate_invoice_data(data)
    assert is_valid is True
    assert error is None


def test_missing_field():
    data = {
        "vendor_name": "ABC",
        "amount": 100
    }

    is_valid, error = validate_invoice_data(data)
    assert is_valid is False
    assert "Missing field" in error
