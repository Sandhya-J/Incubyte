from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from string_calculator import StringCalculator
import uvicorn

app = FastAPI(
    title="String Calculator API",
    description="API for string calculation",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

calculator = StringCalculator()

class CalculateRequest(BaseModel):
    numbers: str

class CalculateResponse(BaseModel):
    result: int

class ErrorResponse(BaseModel):
    error: str

@app.get("/")
async def root():
    """Health check"""
    return {"message": "String Calculator API is running!"}

@app.post("/calculate", response_model=CalculateResponse)
async def calculate(request: CalculateRequest):
    try:
        result = calculator.add(request.numbers)
        return CalculateResponse(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except OverflowError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
