import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import json
from models import Publisher, Book, Shop, Stock, Sale, create_tables
from test_data import insert_data


def get_shop(session, publisher_name):
    query = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).
             join(Publisher, Book.id_publisher == Publisher.id).
             join(Stock, Book.id == Stock.id_book).
             join(Shop, Stock.id_shop == Shop.id).
             join(Sale, Stock.id == Sale.id_stock)
             )
    if publisher_name.isdigit():
        final_query = query.filter(Publisher.id == publisher_name)
    else:
        final_query = query.filter(Publisher.name.like(publisher_name))
    for title, name, price, date_sale in final_query:
        print(f'{title} | {name} | {price} | {date_sale}')

def insert_from_json(session):
    with open('tests_data.json', 'r') as f:
        data = json.load(f)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()



if __name__ == '__main__':
    load_dotenv()
    DSN = os.getenv("DSN")

    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    insert_data(session)
    publisher_name = input('Введите id или фамилию автора: ')
    get_shop(session, publisher_name)

    session.close()
