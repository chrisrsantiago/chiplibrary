# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Boolean,
    Unicode,
    UnicodeText,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from ..lib.reference import Game, Classification
from .cache import RelationshipCache
from .meta import Base

from . import Chip, ChipCode, User

__all__ = ['Folder', 'FolderChip', 'FolderComment']

class Folder(Base):
    __tablename__ = 'folder'

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
        doc='''The display name for this folder.'''
    )
    slug = Column(
        Unicode(50),
        nullable=False,
        doc='''The URL used to access this folder.'''
    )
    game = Column(
        Enum(Game),
        nullable=False,
        doc='''The game for which the folder was intended.'''
    )
    description = Column(
        UnicodeText,
        nullable=False,
        doc='''A brief description of the folder and its intentions.'''
    )
    content = Column(
        UnicodeText,
        nullable=False,
        doc='''A detailed summary of the folder and its uses.'''
    )
    posted = Column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        doc='''The date the folder was posted.'''
    )

    comments = relationship(
        lambda: FolderComment,
        cascade='save-update, merge, delete'
    )
    chips = relationship(
        lambda: FolderChip,
        cascade='save-update, merge, delete'
    )

    __table_args__ = (
        UniqueConstraint('slug', 'game', name='foldername'),
    )
    
    def __init__(self, id_author=None, name=None, game=None,
        description=None, summary=None
    ):
        self.id_author = id_author
        self.name = name
        if not slug:
            slug = self.name
        self.slug = normalize_slug(slug)
        self.game = game
        self.description = description
        self.content = content

class FolderChip(Base):
    __tablename__ = 'folder_chip'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_folder = Column(
        Integer,
        ForeignKey(Folder.id),
        nullable=False,
        doc='''See `chiplibrary.db.folder.Folder` for more information'''
    )
    chip_indice = Column(
        Integer,
        ForeignKey(Chip.indice),
        nullable=False,
        doc='''See `chiplibrary.db.chip.Chip` for more information.  While we
        would typically use the Chip.id field, this number can be somewhat
        unpredictable, and so an indice and classification is best used.'''
    )
    chip_code = Column(
        Unicode(1),
        nullable=False,
        doc='''The chip's specific chip code for this folder.'''
    )
    chip_classification = Column(
        Enum(Classification),
        nullable=True,
        doc='''See `chiplibrary.db.chip.Chip` for more information'''
    )
    chip_regular = Column(Boolean, nullable=True,
        doc='''(BN2+) Indicate whether this is the regular chip for the
        folder. Optional.'''
    )
    chip = relationship(
        lambda: Chip,
        primaryjoin='''and_(
            FolderChip.chip_classification == foreign(Chip.classification),
            FolderChip.chip_indice == Chip.id, 
            Folder.game == Chip.game,
        )''',
        cascade='save-update, merge, delete'
    )
    __table_args__ = (
        # There can only be one regular chip per folder.
        UniqueConstraint('id_folder', 'chip_regular', name='regularchip'),
    )
    
    def __init__(self, id_folder=None, chip_classification=None, chip_code=None,
        chip_regular=None
    ):
        self.id_folder = id_folder
        self.indice_chip = indice_chip
        self.chip_classification = chip_classification
        self.chip_code = chip_code
        self.chip_regular = chip_regular

class FolderComment(Base):
    __tablename__ = 'folder_comment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_folder = Column(
        Integer,
        ForeignKey(Folder.id),
        nullable=False,
        doc='''See `chiplibrary.db.folder.Folder` for more information'''
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
    
    def __init__(self, id_folder=None, id_author=None, content=None):
        self.id_folder = id_folder
        self.id_author = id_author
        self.content = content

cached_bits = RelationshipCache(Folder.chips, 'default') \
    .and_(
            RelationshipCache(FolderChip.chip, 'default')
        )
