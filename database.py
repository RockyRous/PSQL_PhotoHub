from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,  # Подключение к бд
    echo=True  # Логирование
    # pool_size=5,  # Кол-во подключений к бд
    # max_overflow=10  # Дополнительные подключения если 5 уже есть
)

session = sessionmaker(engine)
