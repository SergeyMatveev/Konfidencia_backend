from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Настройка подключения к базе данных
db_uri = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(db_uri)

try:
    # Проверка связи с базой данных
    connection = engine.connect()
    print("Связь с базой данных установлена успешно.")
    connection.close()
except OperationalError as e:
    print("Ошибка при установке связи с базой данных:", e)