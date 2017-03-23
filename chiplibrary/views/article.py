# -*- coding: utf-8 -*-
import transaction

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPInternalServerError,
    HTTPSeeOther,
    HTTPNotFound
)
from sqlalchemy.orm.exc import NoResultFound

from ..db import Article, ArticleComment

from ..lib.auth import login_required, loggedin
from ..lib.forms import ArticleForm, CommentForm, form_errors
from ..lib.reference import Game

@view_config(
    route_name='article_index',
    renderer='../templates/article/index.mako'
)
def index(request):
    articles_result = None

    try:
        game = Game(int(request.matchdict['game']))
        articles_query = request.dbsession.query(Article)
        articles_query = articles_query.filter(
            Article.game == game
        )
        articles_result = articles_query.all()
    except (ValueError, NoResultFound):
        pass

    return {'articles': articles_result}

@view_config(
    route_name='article_add',
    renderer='../templates/article/add.mako'
)
@login_required
def add(request):
    form = ArticleForm(request.POST)
    try:
        game = Game(int(request.matchdict['game']))
    except ValueError:
        raise HTTPNotFound()

    if request.POST:
        if form.validate():
            with transaction.manager:
                article_add = Article(
                    name=form.name.data,
                    id_author=request.user.id,
                    game=game,
                    description=form.description.data,
                    content=form.content.data
                )
                request.dbsession.add(article_add)
            request.dbsession.flush()
            raise HTTPSeeOther(
                location=request.route_path(
                    'article_view',
                    game=article_add.game.value,
                    id=article_add.id
                )
            )
        else:
            for error_message in form_errors(form):
                request.session.flash(error_message, 'errors')
    else:
        pass
    return {'form': form}

@view_config(
    route_name='article_view',
    renderer='../templates/article/view.mako'
)
def view(request):
    article_result = None
    comment_form = CommentForm(request.POST)

    try:
        game = Game(int(request.matchdict['game']))
        article_query = request.dbsession.query(Article)
        article_query = article_query.filter(
            Article.game == game,
            Article.id == request.matchdict['id']
        )
        article_result = article_query.one()
        
        if request.user:
            if request.POST:
                if comment_form.validate():
                    with transaction.manager:
                        comment_add = ArticleComment(
                            id_article=article_result.id,
                            id_author=request.user.id,
                            content=comment_form.comment.data
                        )
                        request.dbsession.add(comment_add)
                    request.dbsession.flush()
                    raise HTTPSeeOther(
                        location=request.current_route_path(
                            _anchor='comment-%s' % (comment_add.id)
                        )
                    )
                else:
                    for error_message in form_errors(comment_form):
                        request.session.flash(error_message, 'errors')
            
    except (ValueError, NoResultFound):
        raise HTTPNotFound()

    return {'article': article_result, 'comment_form': comment_form}
