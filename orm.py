from models import metadata, Base, Posts, Users, Followers, Comments, Categories, PhotoCategories
from database import session, engine
from sqlalchemy import select


def create_table():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = True


def insert_data():
    with session():
        worker_admin = WorkersOrm(username="admin")
        worker_kiril = WorkersOrm(username="Kiril")
        worker_semyon = WorkersOrm(username="Semyon")

        # ses.add(worker_admin)
        session.add_all([worker_admin, worker_kiril, worker_semyon])
        session.flush()
        session.commit()


def select_worker():
    with session():
        # worker_id = 1
        # worker_admin = session.get(WorkersOrm, worker_id)

        query = select(WorkersOrm)
        res = session.execute(query).all()
        print(f'{res=}')


def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
    with session():
        worker_2 = session.get(WorkersOrm, worker_id)  # Берем экземпляр
        worker_2.username = new_username  # Меняем параметры
        session.commit()
