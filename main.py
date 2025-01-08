from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Модель данных для входных данных
class CalculationRequest(BaseModel):
    number1: float
    number2: float

# Создаем экземпляр FastAPI
app = FastAPI()

# Подключение шаблонов и статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Главная страница с UI
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
