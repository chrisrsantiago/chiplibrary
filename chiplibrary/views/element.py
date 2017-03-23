# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from ..lib.reference import elements

@view_config(
    route_name='elements',
    renderer='../templates/element/index.mako'
)
def index(request):
    return {}
