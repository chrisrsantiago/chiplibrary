# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from ..lib.reference import elements

@view_config(
    route_name='element_index',
    renderer='../templates/element/index.mako'
)
def index(request):
    return {}

@view_config(
    route_name='element_view',
    renderer='../templates/element/view.mako'
)
def view(request):
    element = {}
    try:
        element = elements[request.matchdict['name']]
    except KeyError:
        raise HTTPNotFound()
    return {'element': element}
