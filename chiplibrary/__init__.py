# -*- coding: utf-8 -*-
import os

from pyramid.config import Configurator
from pyramid.events import BeforeRender

from .lib import helpers

def add_renderer_globals(event):
    """Template globals.
    """
    event['h'] = helpers
    
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    settings_ = config.get_settings()
    # In case certain directories aren't set in the config, we can default to
    # making one in the same directory as the config file.
    config.add_settings({
        'config_path': os.path.dirname(global_config['__file__'])
    })
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_mako')
    config.include('pyramid_dogpile_cache2')
    config.include('.db')
    config.include('.routes')
    config.include('.lib.search')
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.scan()
    return config.make_wsgi_app()
