# -*- coding: utf-8 -*-
import os

from pyramid.response import FileResponse
from pyramid.view import view_config
from sqlalchemy.orm.exc import NoResultFound

@view_config(route_name='index', renderer='../templates/index.mako')
def index(request):
    return {'title': 'Home'}
    
@view_config(route_name='about', renderer='../templates/about.mako')
def about(request):
    return {'title': 'About'}
    
@view_config(route_name='credits', renderer='../templates/credits.mako')
def credits(request):
    return {'title': 'Credits'}
