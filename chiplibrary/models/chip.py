# -*- coding: utf-8 -*-
import string
import enum

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Boolean,
    Enum,
    Unicode,
    UnicodeText
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

from .meta import metadata, Base

# Possible chip codes: A-Z or * (wildcard symbol)
CODES = list(string.ascii_uppercase)
CODES.append('*')
# Element weaknesses.
# todo: keep these definitions in their own module.
weaknesses = {
    'aqua'      : 'electric',
    'break'     : 'cursor',
    'cursor'    : 'wind',
    'electric'  : 'wood',
    'fire'      : 'aqua',
    'sword'     : 'break',
    'wind'      : 'sword',
    'wood'      : 'fire'
}

__all__ = [
    'Chip',
    'ChipCodes',
    'ChipEffects',
    'Classification',
    'Games',
    'Elements'
]

class Elements(enum.Enum):
    """Chip Elements"""
    null = 1
    aqua = 2
    breaking = 3
    cursor = 4
    electric = 5
    fire = 6
    invisible = 7
    obstacle = 8
    plus = 9
    recovery = 10
    sword = 11
    terrain = 12
    wind = 13
    wood = 14
    
class Classification(enum.Enum):
    """Chip Classifications
    
    standard - The regular set of chips in the game.

    mega (BN3+) - Usually navi chips or stronger chips, these tend to have more
    limits as a side-effect for power.
    
    giga (BN3+) - The strongest chips in the game; usually the rarest, and
    limited to one per folder.
    
    secret - (BN4-BN5) Tend to be navi chips, but unobtainable through regular
    means.

    dark - (BN5) Powerful chips that tend to come with temporary/permanent
    negative side-effects for the player.
    """
    standard = 1
    mega = 2
    giga = 3
    secret = 4
    dark = 5

class Games(enum.Enum):
    """Valid games."""
    bn1 = 1
    bn2 = 2
    bn3 = 3
    bn4 = 4
    bn5 = 5
    bn6 = 6

class Chip(Base):
    """Battle Chips
    
    Since battle chips across all six games vary in just about every
    aspect, we will separate the chip attributes into their own models, with
    all of them referencing a id_chip (``chiplibrary.models.chip.Chip.id``).
    """
    __tablename__ = 'chip'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    indice = Column(Integer, nullable=False,
        doc=u'The in-game number for the chip.'
    )
    game = Column(Enum(Games), nullable=False,
        doc=u'''The game where the chip is from'''
    )
    name = Column(Unicode(50), doc=u'The in-game name for the chip.')
    codes = relationship(lambda: ChipCodes, lazy='dynamic')
    classification = Column(Enum(Classification), nullable=False,
        doc=u'''The in-game classification of a chip (standard, mega, etc.)
        Valid chip types can be found in the Classifications Enum.'''
    )
    effects = relationship(lambda: ChipEffects, lazy='dynamic')
    element = Column(Enum(Elements), nullable=False,
        doc=u'''The element for the chip, can be any element found in Elements
        enum.'''
    )
    size = Column(Integer, doc=u'The size (in MB) of the chip')
    description = Column(UnicodeText(255, convert_unicode=True), nullable=False,
        doc=u'The in-game description for the chip.'
    )
    summary = Column(UnicodeText(convert_unicode=True), nullable=False,
        doc=u'A more detailed explanation of what the battlechip does.'
    )
    stars = Column(Integer, doc=u'The amount of stars for chip.')
    damage = Column(Integer, doc=u'The amount of damage the chip deals.')
    recovery = Column(Integer,
        doc=u'If a recovery chip, the amount of HP recovered.'
    )

class _ChipBase(object):
    """Base table for battle chips, containing columns that are seen in all
    chip_* tables.
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    game = Column(Enum(Games), nullable=False,
        doc=u'''The game where the chip is from'''
    )
    
    @declared_attr
    def id_chip(cls):
        return Column(Integer, ForeignKey(Chip.id), nullable=False,
            doc=u'''See `chiplibrary.models.chip.Chip` for more information'''
        )

ChipBase = declarative_base(metadata=metadata, cls=_ChipBase)
    
class ChipCodes(ChipBase):
    __tablename__ = 'chip_codes'

    code = Column(Unicode(1), nullable=False,
        doc=u'''The chip code for said battlechip.  Varies between games, and
        a chip can contain as many as six different chip codes.  The possible
        values are the letters A-Z, or a wildcard (*).'''
    )

class ChipEffects(ChipBase):
    __tablename__ = 'chip_effects'
    
    flinch = Column(Boolean, nullable=False,
        doc=u'''Whether chip causes flinching (flickering player visibility
        back and forth.)'''
    )
    timestop = Column(Boolean, nullable=False,
        doc=u'Whether chip freezes the battle temporarily (i.e. Navi chips)'
    )
    paralyze = Column(Boolean, nullable=False,
        doc=u'Whether chip causes paralysis, usually from elec element chips.'
    )
    push = Column(Boolean, nullable=False,
        doc=u'Whether chip pushes the player back.'
    )
