# -*- coding: utf-8 -*-
import transaction
from functools import wraps

from pyramid.settings import aslist
from pyramid.events import subscriber, BeforeRender
from pyramid.httpexceptions import HTTPSeeOther, HTTPNotFound, HTTPForbidden

from social.apps.pyramid_app.utils import backends

from ..db import User

class NotLoggedIn(Exception):
    """Raised when a user attempts to view a page and is not logged in."""
    pass

def login_user(backend, user, user_social_auth):
    backend.strategy.session_set('user_id', user.id)

def loggedin(request):
    return getattr(request, 'user', None) is not None

def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not loggedin(request):
            raise NotLoggedIn()
        return func(request, *args, **kwargs)
    return wrapper

def save_user(backend, user, response, *args, **kwargs):
    """python-social-auth doesn't actually save users to the database, so we
    will handle this ourselves via pipeline."""
    with transaction.manager:
        kwargs['social']._session().add(kwargs['social'])
    return

def get_user(request):
    try:
        user_id = request.session['user_id']
        user_query = request.dbsession.query(User)
        user_query = user_query.filter(User.id == user_id)
        user = user_query.first()
    except KeyError:
        user = None
    return user

@subscriber(BeforeRender)
def add_social(event):
    request = event['request']
    event['social'] = backends(request, request.user)

SOCIAL_AUTH_SETTINGS = {
    'SOCIAL_AUTH_LOGIN_URL': '/login',
    'SOCIAL_AUTH_LOGIN_REDIRECT_URL': '/my',
    'SOCIAL_AUTH_USER_MODEL': 'chiplibrary.db.User',
    'SOCIAL_AUTH_LOGIN_FUNCTION': 'chiplibrary.lib.auth.login_user',
    'SOCIAL_AUTH_LOGGEDIN_FUNCTION': 'chiplibrary.lib.auth.loggedin',
    'SOCIAL_AUTH_AUTHENTICATION_BACKENDS': [],
    'SOCIAL_AUTH_PIPELINE': (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'chiplibrary.lib.auth.save_user'
    )
}

def includeme(config):
    SOCIAL_AUTH_SETTINGS['SOCIAL_AUTH_AUTHENTICATION_BACKENDS'] = aslist(
        config.registry.settings['psa.authentication_backends']
    )
    
    SOCIAL_AUTH_KEYS = {
        'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY': config.registry.settings['psa.google.key'],
        'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET': config.registry.settings['psa.google.secret'],

        'SOCIAL_AUTH_TWITTER_KEY': config.registry.settings['psa.twitter.key'],
        'SOCIAL_AUTH_TWITTER_SECRET': config.registry.settings['psa.twitter.secret'],

        'SOCIAL_AUTH_FACEBOOK_APP_KEY': config.registry.settings['psa.facebook.app.key'],
        'SOCIAL_AUTH_FACEBOOK_APP_SECRET': config.registry.settings['psa.facebook.app.secret'],
        'SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE': config.registry.settings['psa.facebook.app.namespace'],

        'SOCIAL_AUTH_YAHOO_OAUTH_KEY': config.registry.settings['psa.yahoo.key'],
        'SOCIAL_AUTH_YAHOO_OAUTH_SECRET': config.registry.settings['psa.yahoo.secret'],

        'SOCIAL_AUTH_LINKEDIN_KEY': config.registry.settings['psa.linkedin.key'],
        'SOCIAL_AUTH_LINKEDIN_SECRET': config.registry.settings['psa.linkedin.secret'],
        'SOCIAL_AUTH_LINKEDIN_SCOPE': aslist(config.registry.settings['psa.linkedin.scope']),

        'SOCIAL_AUTH_GITHUB_KEY': config.registry.settings['psa.github.key'],
        'SOCIAL_AUTH_GITHUB_SECRET': config.registry.settings['psa.github.secret'],

        'SOCIAL_AUTH_INSTAGRAM_KEY': config.registry.settings['psa.instagram.key'],
        'SOCIAL_AUTH_INSTAGRAM_SECRET': config.registry.settings['psa.instagram.secret'],

        'SOCIAL_AUTH_FLICKR_KEY': config.registry.settings['psa.flickr.key'],
        'SOCIAL_AUTH_FLICKR_SECRET': config.registry.settings['psa.flickr.secret'],

        'SOCIAL_AUTH_REDDIT_KEY': config.registry.settings['psa.reddit.key'],
        'SOCIAL_AUTH_REDDIT_SECRET': config.registry.settings['psa.reddit.secret'],
        'SOCIAL_AUTH_REDDIT_AUTH_EXTRA_ARGUMENTS': {},
        
        'SOCIAL_AUTH_STEAM_API_KEY': config.registry.settings['psa.steam.key'],
        'SOCIAL_AUTH_STEAM_EXTRA_DATA': aslist(config.registry.settings['psa.steam.extra'])
    }
    config.registry.settings.update(SOCIAL_AUTH_SETTINGS)
    config.registry.settings.update(SOCIAL_AUTH_KEYS)
