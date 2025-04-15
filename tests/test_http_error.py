import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from fastapi.requests import Request

# Create the test app with the error handler
app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "path": request.url.path},
    )

@app.get("/cause-error")
def cause_error():
    raise HTTPException(status_code=418, detail="I am a teapot")

client = TestClient(app)

def test_http_exception_handler():
    response = client.get("/cause-error")
    assert response.status_code == 418
    assert response.json() == {
        "detail": "I am a teapot",
        "path": "/cause-error"
    }
