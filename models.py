from datetime import datetime
from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


metadata = MetaData()

str_256 = Annotated[str, 256]


# Декларативный стиль
class Base(DeclarativeBase):
    # Создаем свои типы данных, чтобы не дублировать код в таблицы
    type_annotation_map = {
        str_256: String(256)
    }


# Создаем свои типы данных, чтобы не дублировать код в таблицы
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                               onupdate=datetime.utcnow)]  # Подставляет значение само


class Users(Base):
    """ Сами пользователи """
    __tablename__ = 'users'

    UserID: Mapped[intpk]
    Username: Mapped[str]
    Password: Mapped[str]
    Email: Mapped[str]
    FullName: Mapped[str]
    Bio: Mapped[str] = mapped_column(nullable=True)  # Может быть = 0


class Posts(Base):
    """ Посты с фото """
    __tablename__ = 'posts'

    PostID: Mapped[intpk]
    UserID: Mapped[int] = mapped_column(ForeignKey('users.UserID', ondelete='CASCADE'))
    Content: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    URL: Mapped[str]


class Comments(Base):
    """ Комментарии к постам """
    __tablename__ = 'comments'

    CommentID: Mapped[intpk]
    PostID: Mapped[int] = mapped_column(ForeignKey('posts.PostID', ondelete='CASCADE'))
    UserID: Mapped[int] = mapped_column(ForeignKey('users.UserID', ondelete='CASCADE'))
    Text: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class Followers(Base):
    """ Связи подписчиков """
    __tablename__ = 'followers'

    FollowerID: Mapped[intpk]
    UserID: Mapped[int] = mapped_column(ForeignKey('users.UserID', ondelete='CASCADE'))
    FollowerUserID: Mapped[int] = mapped_column(ForeignKey('users.UserID', ondelete='CASCADE'))


class Categories(Base):
    """ Категории для постов """
    __tablename__ = 'categories'

    CategoryID: Mapped[intpk]
    CategoryName: Mapped[str]


class PhotoCategories(Base):
    """ Связь многие-к-многим категории-посты """
    __tablename__ = 'photo_categories'

    PhotoCategoryID: Mapped[intpk]
    PostID: Mapped[int] = mapped_column(ForeignKey('posts.PostID', ondelete='CASCADE'))
    CategoryID: Mapped[int] = mapped_column(ForeignKey('categories.CategoryID', ondelete='CASCADE'))