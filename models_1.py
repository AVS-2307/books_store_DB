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


class Book(Base):
    __tablename__ = 'books'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publishers = relationship("publisher", backref="books")


class Stock(Base):
    __tablename__ = 'stocks'

    id = sq.Column(sq.Integer, primary_key=True)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship("books", backref="stocks")
    shops = relationship("shops", backref="stocks")


class Shop(Base):
    __tablename__ = 'shops'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Sale(Base):
    __tablename__ = 'sales'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship("stocks", backref="sales")
