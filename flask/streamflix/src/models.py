from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    
    def __init__(self, name: str, account_id: int):
        self.name = name
        self.account_id = account_id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'account_id': self.account_id
        }

movies_users_table = db.Table(
    'movies_users',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'movie_id', db.Integer,
        db.ForeignKey('movies.id'),
        primary_key=True
    )
)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False) 
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False) 
    my_stuff_id = db.Column(db.Integer, db.ForeignKey('my_stuff.id'))

    def __init__(self, title: str, rating: int, genre_id: int, my_stuff_id: int):
        self.title = title
        self.rating = rating
        self.genre_id = genre_id
        self.my_stuff_id = my_stuff_id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'rating': self.rating,
            'genre_id': self.genre_id,
            'my_stuff_id': self.my_stuff_id
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class MyStuff(db.Model):
    __tablename__ = 'my_stuff'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Integer, nullable=False)
    added = db.Column(db.Boolean, nullable=False)

    def __init__(self, capacity: int, added: bool):
        self.capacity = capacity
        self.added = added

    def serialize(self):
        return {
            'id': self.id,
            'capacity': self.capacity,
            'added': self.added
        }