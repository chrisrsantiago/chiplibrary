# -*- coding: utf-8 -*-
from pyramid.view import view_config
from sqlalchemy.orm.exc import NoResultFound

@view_config(route_name='index', renderer='index.mako')
def index(request):
    return {'title': 'Home'}
    
@view_config(route_name='about', renderer='about.mako')
def about(request):
    return {'title': 'About'}
    
@view_config(route_name='credits', renderer='credits.mako')
def credits(request):
    return {'title': 'Credits'}
