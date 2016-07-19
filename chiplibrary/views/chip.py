# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from sqlalchemy.orm.exc import NoResultFound

from ..lib import helpers as h

from ..models import Chip
from ..models.chip import Games

@view_config(route_name='chip_index', renderer='chip/index.mako')
def index(request):
    return {'result': [], 'title': u'Chips'}

@view_config(route_name='chip_index_game', renderer='chip/index.mako')
def index_game(request):
    result = []
    try:
        game = Games(int(request.matchdict['game']))
        result = request.dbsession.query(Chip).filter(
            Chip.game == game
        ).all()
    except NoResultFound:
        pass
    return {
        'result': result,
        'title': u'Chips: Battle Network %s' % (request.matchdict['game'],)
    }
    
@view_config(route_name='chip_view', renderer='chip/view.mako')
def view(request):
    try:
        result = request.dbsession.query(Chip).filter(
            Chip.name == request.matchdict['name']
        ).order_by(Chip.game.asc()).all()
    except (NoResultFound):
        raise HTTPNotFound()
    return {
        'chip': result,
        'title': 'Viewing chip: %s' % (chip.name,)
    }

@view_config(route_name='chip_view_game', renderer='chip/view.mako')
def view_game(request):
    try:
        game = Games(int(request.matchdict['game']))
        result = request.dbsession.query(Chip).filter(
            Chip.game == game and Chip.name == request.matchdict['name']
        ).one()
    except (NoResultFound):
        raise HTTPNotFound()

    return {
        'chip': result,
        'title': u'Viewing chip: %s' % (result.names[0].name,)
    }
