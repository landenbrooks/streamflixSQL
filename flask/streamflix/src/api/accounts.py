from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, movies_users_table, Movie, Genre, MyStuff

import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@bp.route('', methods=['GET']) 
def index():
    accounts = Account.query.all() 
    result = []
    for a in accounts:
        result.append(a.serialize()) 
    return jsonify(result) 

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Account.query.get_or_404(id)
    return jsonify(a.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'email' not in request.json or 'password' not in request.json:
        return abort(400)

    if len(request.json['email']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    a = Account(
        email=request.json['email'],
        password=scramble(request.json['password'])
    )
    db.session.add(a) 
    db.session.commit() 
    return jsonify(a.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) 
        db.session.commit() 
        return jsonify(True)
    except:
        return jsonify(False)