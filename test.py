from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Модель запроса с номером телефона
class PhoneNumber(BaseModel):
    phone: str


# Модель запроса с кодом подтверждения
class ConfirmationCode(BaseModel):
    code: str


# Функция для отправки кода подтверждения с использованием стороннего сервиса
def send_confirmation_code(phone_number):
    # Здесь будет отправка кода подтверждения с использованием стороннего сервиса SMS или пуш
    # на вход берем номер телефона, отправляем на него код и ждем ответ verify_confirmation_code
    print("Код отправлен")
    return "123456"


# Конечная точка для отправки кода подтверждения
@app.post("/send-confirmation-code")
def send_confirmation_code_endpoint(phone_number: PhoneNumber):
    # Здесь вы можете добавить проверки и валидацию номера телефона
    print(phone_number + "MSG")

    send_confirmation_code(phone_number.phone)
    return {"message": "Confirmation code has been sent"}


# Конечная точка для проверки введенного кода подтверждения
@app.post("/verify-confirmation-code")
def verify_confirmation_code(confirmation_code: ConfirmationCode):
    # Здесь вы можете добавить логику для проверки введенного кода подтверждения

    # Пример проверки, сравнивая введенный код с жестко заданным значением
    if confirmation_code.code == '123456':
        return {"message": "Confirmation code is correct"}
    else:
        return {"message": "Invalid confirmation code"}





# База данных пользователей (заглушка)
users_db = [
    User(phone="123", name="Мария Матвеева", email="mariamatveeva@gmail.com"),
    User(phone="777", name="Сергей Матвеев", email="matveev.sa@gmail.com")
]


# Конечная точка для поиска пользователя по номеру телефона
@app.get("/users/{phone_number}")
def get_user_by_phone(phone_number: str):
    # Ищем пользователя с указанным номером телефона в базе данных

    for user in users_db:
        if user.phone == phone_number:
            return user

    # Если пользователь не найден, возбуждаем ошибку 404

    raise HTTPException(status_code=404, detail="User not found")
