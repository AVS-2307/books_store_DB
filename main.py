import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker

from models_1 import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = os.getenv(key='DATABASE_URL', default='postgresql://postgres:postgres@localhost:5432/ORM_db')

engine = sqlalchemy.create_engine(DSN)

con = engine.connect

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
publisher_1 = Publisher(name="АСТ")
publisher_2 = Publisher(name="ЭКСМО")
publisher_3 = Publisher(name="Просвещение")
# session.add_all([publisher_1, publisher_2, publisher_3])

book_1 = Book(title="Б. Акунин - Дорога в Китеж", publisher_id=100)
book_2 = Book(title="Б. Акунин - Просто Маса", publisher_id=100)
book_3 = Book(title="Дж.Оруэлл - 1984", publisher_id=101)
book_4 = Book(title="Дж.Оруэлл - Скотный двор", publisher_id=101)
book_5 = Book(title="Англо-русский словарь", publisher_id=102)
# session.add_all([book_1, book_2, book_3, book_4, book_5])

stock_1 = Stock(shop_id=1, book_id=11, count=10)
stock_2 = Stock(shop_id=1, book_id=22, count=20)
stock_3 = Stock(shop_id=1, book_id=33, count=30)
stock_4 = Stock(shop_id=2, book_id=44, count=40)
stock_5 = Stock(shop_id=2, book_id=55, count=50)

# session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5])
shop_1 = Shop(name="Библиоглобус")
shop_2 = Shop(name="Лабиринт")
shop_3 = Shop(name="Литрес")
# session.add_all([shop_1, shop_2, shop_3])


sale_1 = Sale(price=500, date_sale="2022-06-23", stock_id=1, count=3)
sale_2 = Sale(price=600, date_sale="2022-06-22", stock_id=2, count=2)
sale_3 = Sale(price=350, date_sale="2022-06-21", stock_id=3, count=3)
sale_4 = Sale(price=250, date_sale="2022-06-20", stock_id=4, count=4)
sale_5 = Sale(price=2000, date_sale="2022-06-19", stock_id=5, count=25)

# session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5])


session.commit()
session.close()


# Выводит издателя (publisher), имя или идентификатор которого принимается через input()
def req_publisher():
    q = session.query(Publisher).filter(Publisher.name == input("Введите название издательства: "))
    for s in q.all():
        print(s.id, s.name)

    q = session.query(Publisher).filter(Publisher.id == input("Введите Id издательства: "))
    for s in q.all():
        print(s.id, s.name)


# выборка магазинов, продающих целевого издателя
def req_shop_publisher():
    q = session.query(Shop).join(Stock.shop).join(Book.publisher).join(Publisher.name).filter(
        Publisher.name == input("Введите "
                                "название издательства для получения магазина, "
                                "продающего его книги: "))
    for s in q.all():
        print(s.name)


req_shop_publisher()
req_publisher()
