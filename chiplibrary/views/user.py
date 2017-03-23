# -*- coding: utf-8 -*-
import transaction

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPSeeOther
from sqlalchemy.orm.exc import NoResultFound

from ..lib.auth import login_required
from ..db import User

@view_config(route_name='user_login', renderer='../templates/user/login.mako')
def login(request):
    if request.user is not None:
        return HTTPSeeOther(location=request.route_path('index'))
    return {}

@view_config(route_name='user_my', renderer='../templates/user/my.mako')
@login_required
def my(request):
    return {}

@view_config(route_name='user_logout', renderer='string')
@login_required
def logout(request):
    del request.session['user_id']
    return HTTPSeeOther(location=request.route_path('index'))

@view_config(route_name='user_index', renderer='../templates/user/index.mako')
def index(request):
    try:
        users_query = request.dbsession.query(User)
        users_result = users_query.all()
    except NoResultFound:
        request.session.flash('No users found. :(', 'errors')
        raise HTTPSeeOther(location=request.route_path('index'))
    return {'users': users_result}

@view_config(route_name='user_view', renderer='../templates/user/view.mako')
def view(request):
    try:
        user_query = request.dbsession.query(User)
        user_query = user_query.filter(User.id == request.matchdict['id'])
        user_result = user_query.one()
    except NoResultFound:
        request.session.flash('That user does not exist.', 'errors')
        raise HTTPSeeOther(location=request.route_path('index'))

    return {'user': user_result}
