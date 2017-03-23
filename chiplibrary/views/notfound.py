# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.view import notfound_view_config

from ..lib.auth import NotLoggedIn

@notfound_view_config(renderer='../templates/error/404.mako')
def notfound_view(request):
    request.response.status = 404
    return {}

@view_config(context=NotLoggedIn, renderer='../templates/error/notloggedin.mako')
def notloggedin_view(exc, request):
    request.response.status_int = 200
    return {}
