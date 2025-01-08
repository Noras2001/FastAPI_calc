from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Модель данных для входных данных
class CalculationRequest(BaseModel):
    number1: float
    number2: float

# Создаем экземпляр FastAPI
app = FastAPI()


# Главная страница с приветствием
@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в API калькулятора!"}


# Маршрут для сложения
@app.post("/add")
async def add_numbers(request: CalculationRequest):
    result = request.number1 + request.number2
    return {"operation": "addition", "result": result}

# Маршрут для вычитания
@app.post("/subtract")
async def subtract_numbers(request: CalculationRequest):
    result = request.number1 - request.number2
    return {"operation": "subtraction", "result": result}

# Маршрут для умножения
@app.post("/multiply")
async def multiply_numbers(request: CalculationRequest):
    result = request.number1 * request.number2
    return {"operation": "multiplication", "result": result}

# Маршрут для деления
@app.post("/divide")
async def divide_numbers(request: CalculationRequest):
    if request.number2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    result = request.number1 / request.number2
    return {"operation": "division", "result": result}

# Запуск приложения происходит с помощью Uvicorn, например:
# uvicorn main:app --reload
