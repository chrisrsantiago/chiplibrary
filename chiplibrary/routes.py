# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPMovedPermanently

def add_route(config, name, pattern, **kw):
    """Automatically remove the forward-slash to any matched routes by sending a HTTP 301
    response.
    """
    config.add_route(name, pattern, **kw)
    if not pattern.endswith('/'):
        config.add_route(name + '_auto', pattern + '/')
        def redirector(request):
            return HTTPMovedPermanently(
                request.route_url(name, _query=request.GET,
                **request.matchdict)
            )
        config.add_view(redirector, route_name=name + '_auto')

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    add_route(config, 'index', '/')
    add_route(config, 'about', '/about')
    add_route(config, 'credits', '/credits')
    add_route(config, 'user_login', '/login')
    add_route(config, 'user_preferences', '/preferences')
    
    add_route(config, 'chip_index', '/chips')
    add_route(config, 'chip_index_game', '/chips/bn{game:\d+}')
    
    add_route(config, 'chip_view_game', '/chips/bn{game:\d+}/{name}')
    add_route(config, 'chip_view', '/chips/{name}')
    
    add_route(config, 'element_index', '/element')
    add_route(config, 'element_view', '/element/{name}')
