# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Unicode,
    UnicodeText,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from ..lib.reference import Game

from .meta import Base
from . import User

__all__ = ['Article', 'ArticleComment']

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_author = Column(
        Integer,
        ForeignKey(User.id),
        nullable=False,
        doc='''The user ID for the author.'''
    )
    name = Column(
        Unicode(50),
        nullable=False,
        doc='''The display name for this article.'''
    )
    game = Column(
        Enum(Game),
        nullable=False,
        doc='''The game for which the article was intended.'''
    )
    description = Column(
        UnicodeText,
        nullable=False,
        doc='''A brief description of the article and its intentions.'''
    )
    content = Column(
        UnicodeText,
        nullable=False,
        doc='''A detailed summary of the article and its uses.'''
    )
    posted = Column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        doc='''Date and time the comment was posted on.'''
    )
    author = relationship(
        lambda: User,
        cascade='save-update, merge, delete'
    )
    comments = relationship(
        lambda: ArticleComment,
        cascade='save-update, merge, delete',
        lazy='dynamic'
    )

    __table_args__ = (
        UniqueConstraint('name', 'game', name='articlename'),
    )
    
    def __init__(self, id_author=None, name=None, game=None, description=None,
        content=None
    ):
        self.id_author = id_author
        self.name = name
        self.game = game
        self.description = description
        self.content = content

class ArticleComment(Base):
    __tablename__ = 'article_comment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_article = Column(
        Integer,
        ForeignKey(Article.id),
        nullable=False,
        doc='''See `chiplibrary.db.article.Article` for more information'''
    )
    id_author = Column(
        Integer,
        ForeignKey(User.id),
        nullable=False,
        doc='''The user ID for the comment author.'''
    )
    content = Column(
        UnicodeText,
        nullable=False,
        doc='''The comment itself.'''
    )
    posted = Column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        doc='''Date and time the comment was posted on.'''
    )
    author = relationship(
        lambda: User,
        cascade='save-update, merge, delete'
    )

    def __init__(self, id_article=None, id_author=None, content=None):
        self.id_article = id_article
        self.id_author = id_author
        self.content = content
