# -*- coding: utf-8 -*-
from pyramid.view import view_config

@view_config(route_name='index', renderer='../templates/index.mako')
def index(request):
    return {}

@view_config(route_name='about', renderer='../templates/about.mako')
def about(request):
    return {}

@view_config(route_name='credits', renderer='../templates/credits.mako')
def credits(request):
    return {}
