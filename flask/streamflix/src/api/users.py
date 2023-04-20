from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, movies_users_table, Movie, Genre, MyStuff

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'account_id' not in request.json:
        return abort(400)

    u = User(
        name=request.json['name'],
        account_id=request.json['account_id']
    )
    db.session.add(u) 
    db.session.commit() 
    return jsonify(u.serialize())

@bp.route('/<int:id>/movies_users', methods=['GET'])
def movies_users(id: int):
    u = User.query.get_or_404(id)
    result = []
    for m in u.movies_users:
        result.append(m.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) 
        db.session.commit() 
        return jsonify(True)
    except:
        return jsonify(False)