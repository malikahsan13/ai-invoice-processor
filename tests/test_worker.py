from app.services.ai_service import extract_invoice_data


def fake_ai_response(text):
    return {
        "vendor_name": "Test Vendor",
        "invoice_number": "INV-001",
        "amount": 500,
        "due_date": "2024-12-01"
    }


def test_ai_mock(monkeypatch):
    monkeypatch.setattr(
        "app.services.ai_service.extract_invoice_data",
        fake_ai_response
    )

    result = extract_invoice_data("dummy text")

    assert result["vendor_name"] == "Test Vendor"
