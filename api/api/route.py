from flask import Blueprint, request
from .model import db, Gamer


main_bp = Blueprint('main', __name__, url_prefix='/')

@main_bp.route('/flap')
def flap():
    return 'Flapper'

@main_bp.route('/gamers/', methods=['GET'])
def get_gamers():
    gamers = Gamer.query.all()

    output = []
    for gamer in gamers:
        gamer_data = {'username': gamer.username, 'rank': gamer.rank}

        output.append(gamer_data)

    return {"gamers": output}    

@main_bp.route('/gamers/<id>')
def get_gamer(id):
    gamer = Gamer.query.get_or_404(id)
    return {'username': gamer.username, 'rank': gamer.rank}

@main_bp.route('/gamers', methods=['POST'])
def add_gamer():
    gamer = Gamer(
        username = request.json['username'],
        rank = request.json['rank'])
    db.session.add(gamer)
    db.session.commit()
    return {'id': gamer.id, 'msg': 'added successfully'}

@main_bp.route('/gamers/<id>', methods=['DELETE'])
def remove_gamer(id):
    gamer = Gamer.query.get(id)
    if gamer is None:
        return {"error": "gamer not found"}
    db.session.delete(gamer)
    db.session.commit()

    return {'id': gamer.id, 'msg': 'removed successfully'}