# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.view import notfound_view_config

@notfound_view_config(renderer='../templates/error/404.mako')
def notfound_view(request):
    request.response.status = 404
    return {}
    
#@view_config(context=Exception, renderer='../templates/error/500.mako')
def failed_validation(exc, request):
    request.response.status_int = 500
    return {}
