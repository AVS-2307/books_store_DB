import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models_1 import create_tables, Publisher, Shop

DSN = "postgresql://postgres:postgres@localhost:5432/ORM_db"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# создаю издательство
publisher1 = Publisher(name='АСТ')


def req_publisher():
    q = session.query(Publisher).filter(Publisher.name == input("Введите название издательства: "))
    for s in q.all():
        print(s.id, s.name)

    q = session.query(Publisher).filter(Publisher.id == input("Введите Id издательства: "))
    for s in q.all():
        print(s.id, s.name)


def req_shop_publisher():
    q = session.query(Shop).filter(Publisher.name == input("Введите название издательства: "))
    for s in q.all():
        print(s.name)


session.close()

req_shop_publisher()
req_publisher()
