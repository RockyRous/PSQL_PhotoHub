from models import metadata, Base, Posts, Users, Followers, Comments, Categories, PhotoCategories
from database import session, engine
from sqlalchemy import select


"""
Регистрация нового пользователя: Добавление новой записи в таблицу "Users".
Аутентификация пользователя: Проверка соответствия введенных учетных данных с данными в таблице "Users".
Создание нового поста: Добавление записи в таблицу "Posts".
Добавление фотографии к посту: Добавление записи в таблицу "Photos".
Оставление комментария к посту: Добавление записи в таблицу "Comments".
Подписка на пользователя: Добавление записи в таблицу "Followers".
Отписка от пользователя: Удаление записи из таблицы "Followers".
Получение ленты новостей пользователя: Выборка постов от подписанных пользователей.
Получение профиля пользователя: Запрос данных из таблицы "Users".
Поиск пользователей по имени: Выборка из таблицы "Users" с использованием условия LIKE.
Изменение описания пользователя: Обновление записи в таблице "Users".
Удаление поста: Удаление записи из таблицы "Posts" и связанных записей.
Удаление комментария: Удаление записи из таблицы "Comments".
Добавление новой категории: Добавление записи в таблицу "Categories".
Привязка фотографии к категории: Добавление записи в таблицу "PhotoCategories".
Изменение пароля пользователя: Обновление записи в таблице "Users".
Получение списка подписчиков пользователя: Выборка из таблицы "Followers" по UserID.
Получение списка категорий для фотографии: Соединение таблиц "Categories" и "PhotoCategories".
Получение количества лайков для поста: Использование агрегатной функции (например, COUNT) с соединением таблиц.
Получение самых популярных категорий: Анализ количества фотографий в каждой категории
"""


def create_table():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = True


"""
def insert_data():
    with session():
        worker_admin = WorkersOrm(username="admin")
        worker_kiril = WorkersOrm(username="Kiril")
        worker_semyon = WorkersOrm(username="Semyon")

        # ses.add(worker_admin)
        session.add_all([worker_admin, worker_kiril, worker_semyon])
        session.flush()  # Внесение в бд, для дальнейшей связанной логики
        session.commit()


def select_users():
    with session():
        # user_id = 1
        # user_admin = session.get(WorkersOrm, worker_id)

        query = select(WorkersOrm)
        res = session.execute(query).all()
        print(f'{res=}')
        

def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
    with session():
        worker_2 = session.get(WorkersOrm, worker_id)  # Берем экземпляр
        worker_2.username = new_username  # Меняем параметры
        session.commit()
"""