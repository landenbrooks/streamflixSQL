from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, movies_users_table, Movie, Genre, MyStuff

bp = Blueprint('genres', __name__, url_prefix='/genres')

@bp.route('', methods=['GET']) 
def index():
    genres = Genre.query.all() 
    result = []
    for g in genres:
        result.append(g.serialize()) 
    return jsonify(result) 

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Genre.query.get_or_404(id)
    return jsonify(g.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)

    g = Genre(
        name=request.json['name'],
    )
    db.session.add(g) 
    db.session.commit() 
    return jsonify(g.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    g = Genre.query.get_or_404(id)
    try:
        db.session.delete(g) 
        db.session.commit() 
        return jsonify(True)
    except:
        return jsonify(False)
