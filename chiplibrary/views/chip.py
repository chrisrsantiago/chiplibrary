# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

from ..lib.reference import Game
from ..db import Chip
from ..db.cache import FromCache
from ..db.chip import cached_bits

@view_config(route_name='chip_index', renderer='../templates/chip/index.mako')
def index(request):
    return {
        'result': [],
        'settings': {'classifications': False},
    }

@view_config(route_name='chip_index_game', renderer='../templates/chip/index.mako')
def index_game(request):
    result = []
    try:
        game = Game(int(request.matchdict['game']))
        result = request.dbsession.query(Chip) \
            .filter(Chip.game == game) \
            .options(
                FromCache('default'),
                joinedload(Chip.codes),
                cached_bits
            ) \
            .all()
    except (ValueError, NoResultFound):
        pass
    
    classifications = True
    size = True

    if request.matchdict['game'] in ('1', '2'):
        classifications = False
        
        if request.matchdict['game'] == '1':
            size = False
    
    return {
        'chips': result,
        'settings': {'classifications': classifications, 'size': size}
    }
    
#@view_config(route_name='chip_view', renderer='../templates/chip/view.mako')
def view(request):
    try:
        result = request.dbsession.query(Chip) \
            .filter(Chip.name == request.matchdict['name']) \
            .order_by(Chip.game.asc()) \
            .options(
                FromCache('default'),
                joinedload(Chip.codes),
                cached_bits
            ) \
            .all()
    except (NoResultFound):
        raise HTTPNotFound()
        
    return {'chip': result}

@view_config(route_name='chip_view_game', renderer='../templates/chip/view.mako')
def view_game(request):
    try:
        game = Game(int(request.matchdict['game']))
        result = request.dbsession.query(Chip) \
            .filter(Chip.game == game) \
            .filter(Chip.name == request.matchdict['name']) \
            .options(
                FromCache('default'),
                joinedload(Chip.codes),
                cached_bits
            ) \
            .one()
    except (ValueError, NoResultFound):
        raise HTTPNotFound()
        
    return {'chip': result, 'settings': {}}