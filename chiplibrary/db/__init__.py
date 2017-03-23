# -*- coding: utf-8 -*-
from sqlalchemy import engine_from_config
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import configure_mappers

from .user import *
from .chip import *
from .folder import *
from .article import *

from . import cache

# Specify any relationships that couldn't otherwise be specified without all
# models being present.
User.folders = relationship(
    'Folder',
    cascade='save-update, merge, delete',
    lazy='joined'
)

User.articles = relationship(
    'Article',
    cascade='save-update, merge, delete',
    lazy='joined'
)

configure_mappers()

def get_session(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    session_factory = sessionmaker(
        query_cls=cache.query_callable(),
        expire_on_commit=False,
        autocommit=True
    )
    session_factory.configure(bind=engine)
    dbsession = session_factory()
    return dbsession

def includeme(config):
    """Initialize the model for a Pyramid app."""
    settings = config.get_settings()
    config.include('pyramid_tm')
    dbsession = get_session(settings)
    config.registry['dbsession_factory'] = dbsession
    config.add_request_method(lambda d: dbsession, 'dbsession', reify=True)
