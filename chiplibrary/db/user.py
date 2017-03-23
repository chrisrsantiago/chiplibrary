# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Boolean,
    Unicode,
    UnicodeText,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from .meta import Base

__all__ = ['User']

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Unicode(200))
    email = Column(Unicode(200))
    password = Column(Unicode(200), default='')
    name = Column(Unicode(100))
    active = Column(Boolean, default=True)
    
    def __init__(self, username=None, email=None, password=None, name=None,
        active=None
    ):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.active = active
