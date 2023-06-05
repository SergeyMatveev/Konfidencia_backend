from http.client import HTTPException  # Импортируем исключение HTTPException из модуля http.client
from fastapi import FastAPI  # Импортируем класс FastAPI из модуля fastapi
from pydantic import BaseModel  # Импортируем класс BaseModel из модуля pydantic

app = FastAPI(  # Создаем экземпляр FastAPI и указываем название приложения
    title="Konfidencia_backend"
)


def send_confirmation_code(phone_number):
    # Функция для отправки кода подтверждения с использованием стороннего сервиса
    # Здесь будет код отправки кода подтверждения
    return phone_number


class User(BaseModel):
    # Модель данных пользователя с использованием BaseModel
    phone: str
    name: str
    email: str


@app.post("/send-confirmation-code/{phone_number}")
def send_confirmation_code_endpoint(phone_number: int):
    # Конечная точка для отправки кода подтверждения
    # Ожидает номер телефона в качестве параметра
    current_user = User
    current_user.phone = phone_number
    if send_confirmation_code(phone_number):
        return {"message": "Confirmation code has been sent"}
    else:
        return {"message": "Confirmation code has not been sent"}


users_db = [
    User(phone="123", name="Мария Матвеева", email="mariamatveeva@gmail.com"),
    User(phone="777", name="Сергей Матвеев", email="matveev.sa@gmail.com")
]


def get_user_by_phone(phone_number: str):
    # Функция для поиска пользователя по номеру телефона в базе данных
    for user in users_db:
        if user.phone == phone_number:
            return user

    # Если пользователь не найден, возбуждаем ошибку 404
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/verify-confirmation-code/{confirmation_code}")
def verify_confirmation_code(confirmation_code: str):
    # Конечная точка для проверки введенного кода подтверждения
    # Ожидает код подтверждения в качестве параметра пути
    if confirmation_code == '123456':
        # Если код верный, ищем клиента по номеру телефона
        user2 = get_user_by_phone(current_user.phone)
        return {"message": "Confirmation code is valid"}, user2
    else:
        return {"message": "Invalid confirmation code"}


@app.get("/")
def get_mainpage():
    # Конечная точка для получения главной страницы
    return "Main page"
