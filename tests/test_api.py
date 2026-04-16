import pytest

@pytest.mark.asyncio
async def test_upload_invoice(client):
    files = {"file": ("test.pdf",b"dummy content")}
    
    response = await client.post("/invoice/upload-invoice", files=files)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "file_id" in data
    assert data["status"] == "queued"