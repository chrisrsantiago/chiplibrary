# -*- coding: utf-8 -*-
import urllib.parse

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

from ..db import Chip
from ..db.cache import FromCache
from ..db.chip import cached_bits

from ..lib.reference import Game

@view_config(route_name='game', renderer='../templates/game/index.mako')
def index_game(request):
    return {}

@view_config(
    route_name='chip_index',
    renderer='../templates/chip/index.mako'
)
def index(request):
    settings = {
        'classifications': True,
        'size': True,
    }

    if request.matchdict['game'] in ('1', '2'):
        settings['classifications'] = False

        if request.matchdict['game'] == '1':
            settings['size'] = False

    result = []
    try:
        game = Game(int(request.matchdict['game']))
        query = request.dbsession.query(Chip)
        query = query.filter(Chip.game == game)
        query = query.options(
            FromCache('default'),
            joinedload(Chip.codes),
            cached_bits
        )
        result = query.all()
    except (ValueError, NoResultFound):
        raise HTTPNotFound()
    
    return {
        'chips': result,
        'settings': settings
    }

@view_config(route_name='chip_view', renderer='../templates/chip/view.mako')
def view(request):
    try:
        game = Game(int(request.matchdict['game']))
        chip_query = request.dbsession.query(Chip)
        chip_query = chip_query.filter(
            Chip.game == game,
            Chip.name == urllib.parse.unquote(request.matchdict['name'])
        )
        chip_query = chip_query.options(
            FromCache('default'),
            joinedload(Chip.codes),
            cached_bits
        )
        chip_result = chip_query.one()
        # Query the database for battlechips having identical names in other
        # games in case the user might want to compare chips.
        othergames_result = []
        try:
            othergames_query = request.dbsession.query(Chip)
            othergames_query = othergames_query.filter(
                Chip.name == chip_result.name,
                Chip.game != chip_result.game
            )
            othergames_query = othergames_query.options(
                FromCache('default'),
                cached_bits
            )
            othergames_query = othergames_query.order_by(Chip.game.asc())
            othergames_result = othergames_query.all()
        except NoResultFound:
            pass
    except (ValueError, NoResultFound):
        raise HTTPNotFound()
        
    return {'chip': chip_result, 'othergames': othergames_result}
