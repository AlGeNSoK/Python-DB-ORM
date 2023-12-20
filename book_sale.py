import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os
from dotenv import load_dotenv
import json

Base = declarative_base()

# Задание 1
class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True, nullable=False)


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True, nullable=False)


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), unique=True, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="books")


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)

    book = relationship(Book, backref="stocks_book")
    shop = relationship(Shop, backref="stocks_shop")


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)

    stock = relationship(Stock, backref="sales")


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


load_dotenv()
DSN = os.getenv("DSN")

engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Заполнение таблиц
p1 = Publisher(name='Пушкин')
p2 = Publisher(name='Достоевский')
p3 = Publisher(name='Толстой')
p4 = Publisher(name='Булгаков')
session.add_all([p1, p2, p3, p4])
session.commit()

b1 = Book(title='Евгений Онегин', publisher=p1)
b2 = Book(title='Капитанская дочка', publisher=p1)
b3 = Book(title='Руслан и Людмила', publisher=p1)
b4 = Book(title='Дубровский', publisher=p1)
b5 = Book(title='Пиковая дама', publisher=p1)

b6 = Book(title='Преступление и наказание', publisher=p2)
b7 = Book(title='Братья Карамазовы', publisher=p2)
b8 = Book(title='Подросток', publisher=p2)
b9 = Book(title='Белые ночи', publisher=p2)

b10 = Book(title='Анна Каренина', publisher=p3)
b11 = Book(title='Золотой ключик, или Приключения Буратино', publisher=p3)
b12 = Book(title='Война и мир', publisher=p3)
b13 = Book(title='Кавказский пленник. Хаджи-Мурат', publisher=p3)

b14 = Book(title='Мастер и Маргарита', publisher=p4)
b15 = Book(title='Белая гвардия', publisher=p4)
b16 = Book(title='Собачье сердце', publisher=p4)
b17 = Book(title='Морфий', publisher=p4)
session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17])
session.commit()

shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Книжный дом')
session.add_all([shop1, shop2, shop3])
session.commit()

stock1 = Stock(count=50, book=b1, shop=shop1)
stock2 = Stock(count=30, book=b2, shop=shop2)
stock3 = Stock(count=20, book=b3, shop=shop3)
stock4 = Stock(count=40, book=b4, shop=shop1)
stock5 = Stock(count=55, book=b5, shop=shop2)
stock6 = Stock(count=10, book=b6, shop=shop3)
stock7 = Stock(count=15, book=b7, shop=shop1)
stock8 = Stock(count=25, book=b8, shop=shop2)
stock9 = Stock(count=30, book=b9, shop=shop3)
stock10 = Stock(count=20, book=b10, shop=shop1)
stock11 = Stock(count=10, book=b11, shop=shop2)
stock12 = Stock(count=40, book=b12, shop=shop3)
stock13 = Stock(count=25, book=b13, shop=shop1)
stock14 = Stock(count=10, book=b14, shop=shop2)
stock15 = Stock(count=15, book=b15, shop=shop3)
stock16 = Stock(count=20, book=b16, shop=shop1)
stock17 = Stock(count=60, book=b17, shop=shop2)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12,
                 stock13, stock14, stock15, stock16, stock17])
session.commit()

sale1 = Sale(price=191, date_sale='2023-12-01', count=2, stock=stock1)
sale2 = Sale(price=200, date_sale='2023-11-02', count=4, stock=stock2)
sale3 = Sale(price=239, date_sale='2023-09-03', count=3, stock=stock3)
sale4 = Sale(price=288, date_sale='2023-12-04', count=8, stock=stock4)
sale5 = Sale(price=174, date_sale='2023-10-05', count=1, stock=stock5)
sale6 = Sale(price=259, date_sale='2023-12-15', count=2, stock=stock6)
sale7 = Sale(price=296, date_sale='2023-11-02', count=4, stock=stock7)
sale8 = Sale(price=296, date_sale='2023-09-20', count=3, stock=stock8)
sale9 = Sale(price=239, date_sale='2023-12-10', count=8, stock=stock9)
sale10 = Sale(price=296, date_sale='2023-11-05', count=1, stock=stock10)
sale11 = Sale(price=229, date_sale='2023-12-02', count=2, stock=stock11)
sale12 = Sale(price=556, date_sale='2023-11-02', count=4, stock=stock12)
sale13 = Sale(price=219, date_sale='2023-09-03', count=3, stock=stock13)
sale14 = Sale(price=513, date_sale='2023-12-04', count=8, stock=stock14)
sale15 = Sale(price=219, date_sale='2023-10-05', count=1, stock=stock15)
sale16 = Sale(price=494, date_sale='2023-12-04', count=8, stock=stock16)
sale17 = Sale(price=494, date_sale='2023-10-05', count=1, stock=stock17)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12, sale13,
                 sale14, sale15, sale16, sale17])
session.commit()

# Задание 2
publisher_name = input('Введите фамилию автора: ')
query = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).
         join(Publisher, Book.id_publisher == Publisher.id).
         join(Stock, Book.id == Stock.id_book).
         join(Shop, Stock.id_shop == Shop.id).
         join(Sale, Stock.id == Sale.id_stock).filter(Publisher.name.like(publisher_name)))
for title, name, price, date_sale in query:
    print(f'{title} | {name} | {price} | {date_sale}')

# Задание 3
# with open('tests_data.json', 'r') as f:
#     data = json.load(f)
#
# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()


session.close()
