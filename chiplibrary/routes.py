# -*- coding: utf-8 -*-
import os

from pyramid.view import view_config
from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPMovedPermanently

def add_route(config, name, pattern, **kw):
    """Automatically remove the forward-slash to any matched routes by
    sending a HTTP 301 response.
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

def add_redirect(config, old_pattern, name, **kw):
    """Redirect a given route pattern to the new route, keeping into account
    forward-slashes.
    """
    # Account for forward-slashes
    add_route(config, name + '_redirect', old_pattern)
    def redirector(request):
        return HTTPMovedPermanently(
            request.route_url(
                name,
                _query=request.GET,
                **request.matchdict,
                **kw
            )
        )
    config.add_view(redirector, route_name=name + '_redirect')

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # Resources
    add_route(config, 'favicon', '/favicon.ico')
    add_route(config, 'robots', '/robots.txt')
    
    add_route(config, 'index', '/')
    add_route(config, 'about', '/about')
    add_route(config, 'credits', '/credits')
    add_route(config, 'development', '/development')

    add_route(config, 'game', '/bn{game:\d+}')

    add_route(config, 'chip_index', '/bn{game:\d+}/chips')
    add_route(config, 'chip_view', '/bn{game:\d+}/chips/{name}')

    # Redirect old /chips/{game} routes to /{game}/chips
    add_redirect(config, '/chips', 'index')
    add_redirect(config, '/chips/bn{game:\d+}', 'chip_index')
    add_redirect(config, '/chips/bn{game:\d+}/{name}', 'chip_view')

    add_route(config, 'folder_index', '/bn{game:\d+}/folders')
    add_route(config, 'folder_add', '/bn{game:\d+}/folders/add')
    add_route(config, 'folder_view', '/bn{game:\d+}/folders/{id:\d+}')

    add_route(config, 'article_index', '/bn{game:\d+}/articles')
    add_route(config, 'article_add', '/bn{game:\d+}/articles/add')
    add_route(config, 'article_view', '/bn{game:\d+}/articles/{id:\d+}')

    add_route(config, 'elements', '/elements')

    add_route(config, 'search', '/search')
    add_route(config, 'search_autocomplete', '/autocomplete')

    add_route(config, 'user_login', '/login')
    add_route(config, 'user_logout', '/logout')
    add_route(config, 'user_my', '/my')
    add_route(config, 'user_index', '/users')
    add_route(config, 'user_view', '/users/{id:\d+}')
    
    add_route(config, 'social.auth', '/login/{backend}')
    add_route(config, 'social.complete', '/login-complete/{backend}')
    add_route(config, 'social.disconnect', '/user-disconnect/{backend}')
    add_route(config, 'social.disconnect_association',
        '/user-disconnect/{backend}/{association_id}'
    )

@view_config(route_name='favicon')
def favicon(request):
    icon = os.path.join(
        os.path.dirname(__file__),
        'static',
        'favicon.ico'
    )
    return FileResponse(icon, request=request)

@view_config(route_name='robots')
def robots(request):
    robots = os.path.join(
        os.path.dirname(__file__),
        'static',
        'robots.txt'
    )
    return FileResponse(robots, request=request)
