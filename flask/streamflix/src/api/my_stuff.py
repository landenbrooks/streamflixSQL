from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, movies_users_table, Movie, Genre, MyStuff

bp = Blueprint('my_stuff', __name__, url_prefix='/my_stuff')

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    my = MyStuff.query.get_or_404(id)
    if 'capacity' not in request.json and 'added' not in request.json:
        return abort(400)

    if 'capacity' in request.json:
        if request.json['capacity'] > 5:
            return abort(400)
        my.capacity = request.json['capacity']

    if 'added' in request.json: 
        if request.json['added'] == False:
            return abort(400)
        my.added = request.json['added']

    try:
        db.session.commit()
        return jsonify(my.serialize())
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    my = MyStuff.query.get_or_404(id)
    try:
        db.session.delete(my) 
        db.session.commit() 
        return jsonify(True)
    except:
        return jsonify(False)