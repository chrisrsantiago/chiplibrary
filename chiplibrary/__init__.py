# -*- coding: utf-8 -*-
import os

from pyramid.config import Configurator
from pyramid.events import BeforeRender, NewRequest
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.scripts.pviews import PViewsCommand

from social.apps.pyramid_app.models import init_social

from .lib import helpers, reference
from .db import User
from .db.meta import Base

def add_renderer_globals(event):
    """Template globals.
    """
    event['h'] = helpers
    event['r'] = reference

def breadcrumb_subscriber(event):
    """Build breadcrumbs on pageload dynamically, to generate in
    templates via the `request.bread` list..
    """
    pvcomm = PViewsCommand([])

    parts = event.request.path_info.split('/')
    views = []

    for i in range(1, len(parts)):
        path = '/'.join(parts[:i])
        view = pvcomm._find_view(event.request)
        if view:
            if path == '':
                # Root page
                views.append({'url': '/', 'title': 'chiplibrary'})
            else:
                title = path.split('/')[-1]
                
                if title in set(['bn1', 'bn2', 'bn3', 'bn4', 'bn5', 'bn6']):
                    title = title.replace('bn', 'Battle Network ')
                views.append({'url': path, 'title': title.title()})
    # Current Page
    views.append({'url': '', 'title': ''})
    event.request.bread = views

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    settings = config.get_settings()
    # In case certain directories aren't set in the config, we can default to
    # making one in the same directory as the config file.
    config.add_settings({
        'config_path': os.path.dirname(global_config['__file__'])
    })
    session_factory = UnencryptedCookieSessionFactoryConfig(
        settings['session.secret']
    )
    config.set_session_factory(session_factory)
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_mako')
    config.include('pyramid_dogpile_cache2')
    config.include('.db')
    config.include('.routes')
    # Instantiate Whoosh Search Index
    config.include('.lib.search')
    # Setup python-social-auth
    config.add_request_method(
        'chiplibrary.lib.auth.get_user',
        'user',
        reify=True
    )
    config.include('chiplibrary.lib.auth')
    init_social(config, Base, config.registry['dbsession_factory'])
    # Add subscribers to instantiate processes or run necessary startup tasks
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.add_subscriber(breadcrumb_subscriber, NewRequest)
    config.scan()
    config.scan('social_pyramid')
    return config.make_wsgi_app()
