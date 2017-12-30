from sqlalchemy import Column, Integer, String, Text, Numeric

from scraper import Base


class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    serial_number = Column(String(50))
    price = Column(Numeric)
    link = Column(Text)

    def __init__(self, id=None, title=None, serial_number=None, price=None, link=None):
        self.id = id
        self.title = title
        self.serial_number = serial_number
        self.price = price
        self.link = link

    def __repr__(self):
        return '<Book(id={}, title={}, serial_number={}, price={}, link={})>'.format(
            self.id,
            self.title,
            self.serial_number,
            self.price,
            self.link
        )
