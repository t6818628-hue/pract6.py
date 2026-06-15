from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship

engine = create_engine('sqlite:///library.db', echo=True)

print(engine)

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birth_year = Column(Integer)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(name='Стивен Кинг', birth_year=1947)
author2 = Author(name='Джоан Роулинг', birth_year=1965)
author3 = Author(name='Джордж Оруэлл', birth_year=1903)

session.add_all([author1, author2, author3])
session.commit()

book1 = Book(title='Сияние', year=1977, author=author1)
book2 = Book(title='Зелёная миля', year=1996, author=author1)
book3 = Book(title='Гарри Поттер и философский камень', year=1997, author=author2)
book4 = Book(title='Гарри Поттер и Тайная комната', year=1998, author=author2)
book5 = Book(title='1984', year=1949, author=author3)

session.add_all([book1, book2, book3, book4, book5])
session.commit()

authors = session.query(Author).all()
for author in authors:
    print(author.name)

author_to_update = session.query(Author).filter(Author.name == 'Джордж Оруэлл').first()
if author_to_update:
    author_to_update.name = 'Джордж Оруэлл (писатель)'
    session.commit()

book_to_delete = session.query(Book).filter(Book.title == '1984').first()
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()

books_sorted = session.query(Book).order_by(Book.year.desc()).all()
for book in books_sorted:
    print(book.title, book.year)

books_after_1950 = session.query(Book).filter(Book.year > 1950).all()
for book in books_after_1950:
    print(book.title, book.year)

author_by_name = session.query(Author).filter(Author.name == 'Стивен Кинг').first()
if author_by_name:
    print(author_by_name.name, author_by_name.birth_year)

book_count = session.query(func.count(Book.id)).scalar()
print(f'Количество книг: {book_count}')

first_three_books = session.query(Book).order_by(Book.title).limit(3).all()
for book in first_three_books:
    print(book.title)

session.close()