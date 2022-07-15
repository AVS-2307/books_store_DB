import sqlalchemy as sq
from sqlalchemy import PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Publisher(Base):
    __tablename__ = 'publishers'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    books = relationship("books", back_populates="publisher")


class Book(Base):
    __tablename__ = 'books'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publishers = relationship("publisher", back_populates="books")
    stocks = relationship("stocks", secondary='stocksbooks', back_populates="books")


class Stock(Base):
    __tablename__ = 'stocks'

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    # Объявляется отношение многие ко многим к book через промежуточную таблицу stocksbooks
    books = relationship("books", secondary='stocksbooks', back_populates="stocks")
    # Объявляется отношение многие ко многим к shop через промежуточную таблицу Shopsstocks
    shops = relationship("shops", secondary='Shopsstocks', back_populates="stocks")
    sales = relationship("sales", back_populates="stocks")


class Stocksbooks(Base):
    __tablename__ = 'stocksbooks'

    # здесь мы объявляем составной ключ, состоящий из двух полей
    __table_args__ = (PrimaryKeyConstraint('stock.id', 'book.id'),)
    # В промежуточной таблице явно указываются что следующие поля являются внешними ключами
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
    book_id = sq.Column(sq.Integer, sq.ForeignKey('books.id'))


class Shop(Base):
    __tablename__ = 'shops'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    stocks = relationship("stocks", back_populates="shops")


#
#
# class Shopsstocks(Base):
#     __tablename__ = 'Shopsstocks'
#     # здесь мы объявляем составной ключ, состоящий из двух полей
#     __table_args__ = (PrimaryKeyConstraint('shops.id', 'stocks.id'),)
#     # В промежуточной таблице явно указываются что следующие поля являются внешними ключами
#     stock_id = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
#     shop_id = sq.Column(sq.Integer, sq.ForeignKey('shops.id'))
#
#
class Sale(Base):
    __tablename__ = 'sales'
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.DateTime)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
    count = sq.Column(sq.Integer)

    stocks = relationship("stocks", back_populates="sales")
