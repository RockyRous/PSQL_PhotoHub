from models import metadata, Base, Posts, Users, Followers, Comments, Categories, PhotoCategories
from database import session, engine
from sqlalchemy import select, func, cast, and_


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


def insert_data():
    with session() as sess:
        user_1 = Users(username="admin", password="admin", email="admin@mail")
        user_2 = Users(username="petya", password="123", email="petya@mail")
        user_3 = Users(username="vanya", password="123", email="vanya@mail")
        user_4 = Users(username="net", password="2222", email="777")

        # ses.add(user_1)
        sess.add_all([user_1, user_2, user_3, user_4])
        sess.flush()  # Внесение в бд, для дальнейшей связанной логики
        sess.commit()


def select_users():
    with session() as sess:
        query = (select(Users.username).select_from(Users))
        res = sess.execute(query)
        result = res.all()
        print(result)
        

def update_users(user_id: int = 2, new_username: str = 'Misha'):
    with session() as sess:
        worker_2 = sess.get(Users, user_id)  # Берем экземпляр
        worker_2.username = new_username  # Меняем параметры
        sess.commit()


def select_all_users(param: str = "@mail"):
    """

    :return:
    """
    with session() as sess:
        query = (
            select(
                Users.username,
                Users.password.label('Pass'),
                Users.email,
                Users.bio
                # Тут можно описать функцией новый столбец
            )
            .select_from(Users)
            .filter(and_(
                Users.email.contains(param)  # Фильтруем по наличию подстроки
            ))
            # .group_by(Users.password)  # Группировка
        )
        res = sess.execute(query)
        result = res.all()
        print(result)

