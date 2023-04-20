from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, movies_users_table, Movie, Genre, MyStuff

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('', methods=['GET']) 
def index():
    movies = Movie.query.all() 
    result = []
    for m in movies:
        result.append(m.serialize()) 
    return jsonify(result) 

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    m = Movie.query.get_or_404(id)
    return jsonify(m.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'title' not in request.json or 'rating' not in request.json or 'genre_id' not in request.json:
        return abort(400)

    m = Movie(
        title=request.json['title'],
        rating=request.json['rating'],
        genre_id=request.json['genre_id']
    )
    db.session.add(m) 
    db.session.commit() 
    return jsonify(m.serialize())

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    m = Movie.query.get_or_404(id)
    if 'title' not in request.json and 'rating' not in request.json and 'genre_id' not in request.json:
        return abort(400)

    if 'title' in request.json:
        if len(request.json['title']) < 1:
            return abort(400)
        m.title = request.json['title']

    if 'rating' in request.json: 
        if request.json['rating'] < 1 or request.json['rating'] > 100:
            return abort(400)
        m.rating = request.json['rating']

    if 'genre_id' in request.json:
        if request.json['genre_id'] < 1 or request.json['genre_is'] > 4:
            return abort(400)
        m.genre_id = request.json['genre_id']

    try:
        db.session.commit()
        return jsonify(m.serialize())
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    m = Movie.query.get_or_404(id)
    try:
        db.session.delete(m) 
        db.session.commit() 
        return jsonify(True)
    except:
        return jsonify(False)