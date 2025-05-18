"""Entry point for the backend service."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Simple placeholder endpoint."""
    return {"message": "Welcome to the backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
