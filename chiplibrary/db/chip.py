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
    UnicodeText,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

from .cache import RelationshipCache
from .meta import metadata, Base

__all__ = [
    'Chip',
    'ChipBase',
    'ChipCode',
    'ChipEffects',
    'Classification',
    'Games',
    'Elements'
]

class Elements(enum.IntEnum):
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
    
class Classification(enum.IntEnum):
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

class Games(enum.IntEnum):
    """Valid games."""
    bn1 = 1
    bn2 = 2
    bn3 = 3
    bn4 = 4
    bn5 = 5
    bn6 = 6

class Versions(enum.IntEnum):
    """Valid game versions."""
    white = 1
    blue = 2
    redsun = 3
    bluemoon = 4
    colonel = 5
    protoman = 6
    gregar = 7
    falzar = 8    

class Chip(Base):
    """Battle Chips
    
    Since battle chips across all six games vary in just about every
    aspect, we will separate the chip attributes into their own models, with
    all of them referencing a id_chip (``chiplibrary.models.chip.Chip.id``).
    """
    __tablename__ = 'chip'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    indice = Column(
        Integer,
        nullable=False,
        default=0,
        doc=u'''The in-game number for the chip.  Some chips do not have
        an indice as a result of not being officially
        obtainable in the games.'''
    )
    game = Column(
        Enum(Games),
        nullable=False,
        doc=u'''The game where the chip is from.'''
    )
    version = Column(
        Enum(Versions),
        nullable=True,
        doc=u'''Post MMBN2, each MMBN game had version-exclusive chips,
        so we are accounting for those.  In the case that the chip is not
        version is exclusive, this may be left blank.'''
    )
    name = Column(
        Unicode(50),
        nullable=False,
        doc=u'The in-game name for the chip.'
    )
    codes = relationship(
        lambda: ChipCode,
        cascade='save-update, merge, delete'
    )
    classification = Column(
        Enum(Classification),
        nullable=True,
        doc=u'''The in-game classification of a chip (standard, mega, etc.)
        Valid chip types can be found in the Classifications Enum.'''
    )
    effects = relationship(
        lambda: ChipEffects,
        cascade='save-update, merge, delete'
    )
    element = Column(
        Enum(Elements),
        nullable=False,
        doc=u'''The element for the chip, can be any element found in Elements
        enum.'''
    )
    size = Column(
        Integer,
        nullable=False,
        default=0,
        doc=u'The size (in MB) of the chip, from 1-99'
    )
    description = Column(
        UnicodeText(255, convert_unicode=True),
        nullable=False,
        doc=u'The in-game description for the chip.'
    )
    summary = Column(
        UnicodeText(convert_unicode=True),
        nullable=True,
        doc=u'A more detailed explanation of what the battlechip does.'
    )
    rarity = Column(Integer,
        nullable=False,
        default=1,
        doc=u'''The amount of stars (rarity) of a chip, from 1-5.'''
    )
    damage_min = Column(
        Integer,
        nullable=False,
        default=0,
        doc=u'The amount of damage the chip deals by itself. (Minimum)'
    )
    damage_max = Column(
        Integer,
        nullable=False,
        default=0,
        doc=u'The amount of damage the chip deals by itself. (Maximum)'
    )
    recovery = Column(
        Integer,
        nullable=False,
        default=0,
        doc=u'If a recovery chip, the amount of HP recovered.'
    )
    
    __table_args__ = (
        UniqueConstraint('name', 'game', name='chip'),
    )
    
    def __init__(self, indice='', game='', version='', name='',
        classification='', element='', size=0, description='',
        summary='', rarity='', damage_min=0, damage_max=0, recovery=0
    ):
        self.indice = indice
        self.game = game
        self.version = version
        self.name = name
        self.classification = classification
        self.element = element
        self.size = size
        self.description = description
        self.summary = summary
        self.rarity = rarity
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.recovery = recovery
        
    def __repr__(self):
        return u'<Chip: #%s - %s - %s>' % (self.indice, self.name, self.game)

    def codes_iter(self):
        return [code.code for code in self.codes]
    

class _ChipBase(object):
    """Base table for battle chips, containing columns that are seen in all
    chip_* tables.
    """
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    game = Column(
        Enum(Games),
        nullable=False,
        doc=u'''The game where the chip is from'''
    )
    
    @declared_attr
    def id_chip(cls):
        return Column(
            Integer,
            ForeignKey(Chip.id),
            nullable=False,
            default='',
            doc=u'''See `chiplibrary.models.chip.Chip` for more information'''
        )

ChipBase = declarative_base(metadata=metadata, cls=_ChipBase)
    
class ChipCode(ChipBase):
    __tablename__ = 'chip_code'

    code = Column(
        Unicode(1),
        nullable=False,
        doc=u'''The chip code for said battlechip.  Varies between games, and
        a chip can contain as many as six different chip codes.  The possible
        values are the letters A-Z, or a wildcard (*).'''
    )
    
    __table_args__ = (
        UniqueConstraint('id_chip', 'code', 'game', name='chip_code'),
    )
    
    def __init__(self, id_chip, code='', game=''):
        # Possible chip codes: A-Z or * (wildcard symbol)
        code = code.upper()
        CODES = list(string.ascii_uppercase)
        CODES.append('*')
        if code not in CODES:
            raise Exception(
                'Invalid Chip Code: %s.  Only A-Z and * allowed.' % (code)
            )
        self.id_chip = id_chip
        self.code = code
        self.game = game
        
    def __repr__(self):
        return u'<ChipCode: #(%s) - %s - %s>' % (self.id_chip, self.code, self.game)

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
    
    __table_args__ = (
        UniqueConstraint('id_chip', 'game', name='chip_effects'),
    )
    
    def __init__(self, game='', flinch='', timestop='', paralyze='', push=''):
        self.game = game
        self.flinch = flinch
        self.timestop = timestop
        self.paralyze = paralyze
        self.push = push
        
    def __repr__(self):
        return u'<ChipEffects: #(%s) - %s>' % (self.id_chip, self.game)

cached_bits = RelationshipCache(Chip.codes, 'default') \
    .and_(
        RelationshipCache(Chip.effects, 'default')
    )
