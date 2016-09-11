# -*- coding: utf-8 -*-
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
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_mako')
    config.include('pyramid_dogpile_cache2')
    config.include('.db')
    config.include('.lib.cache')
    config.include('.routes')
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.scan()
    return config.make_wsgi_app()
