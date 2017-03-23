# -*- coding: utf-8 -*-
import urllib.parse

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

from ..db import Folder
from ..db.cache import FromCache
from ..db.chip import cached_bits

from ..lib.reference import Game

@view_config(
    route_name='folder_index',
    renderer='../templates/folder/index.mako'
)
def index(request):
    folders_result = None

    try:
        game = Game(int(request.matchdict['game']))
        folders_query = request.dbsession.query(Folder)
        folders_query = folders_query.filter(
            Folder.game == game
        )
        folders_result = folders_query.all()
    except (ValueError, NoResultFound):
        pass

    return {'folders': folders_result}

@view_config(
    route_name='folder_view',
    renderer='../templates/folder/view.mako'
)
def view(request):
    folder_result = None

    try:
        game = Game(int(request.matchdict['game']))
        folder_query = request.dbsession.query(Folder)
        folder_query = folder_query.filter(
            Folder.game == game,
            Folder.slug == request.matchdict['name']
        )
        folder_result = folder_query.one()
    except (ValueError, NoResultFound):
        raise HTTPNotFound()

    return {'folder': folder_result}
