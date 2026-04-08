from fastapi import FastAPI

app = FastAPI(title="AI Invoice Processor")


@app.get("/")
async def root():
    return {"message": "API is running"}
