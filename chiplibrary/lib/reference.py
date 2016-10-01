# -*- coding: utf-8 -*-
"""Game reference variables that don't seem to belong anywhere else."""
import enum
from collections import namedtuple, OrderedDict

__all__ = [
    'Element',
    'Classification',
    'Game',
    'Version',
    'elements',
    'rarities'
]

class Element(enum.IntEnum):
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

class Game(enum.IntEnum):
    """Valid games."""
    bn1 = 1
    bn2 = 2
    bn3 = 3
    bn4 = 4
    bn5 = 5
    bn6 = 6

class Version(enum.IntEnum):
    """Valid game versions."""
    white = 1
    blue = 2
    redsun = 3
    bluemoon = 4
    colonel = 5
    protoman = 6
    doubleteam = 7
    gregar = 8
    falzar = 9

ElementTuple = namedtuple('ElementTuple', 'name introduced weakness strength')
elements = {
    'aqua': ElementTuple('aqua', '1', 'electric', 'fire'),
    'breaking': ElementTuple('breaking', '4', 'cursor', 'sword'),
    'cursor': ElementTuple('cursor', '4', 'wind', 'breaking'),
    'electric': ElementTuple('electric', '1', 'wood', 'aqua'),
    'fire': ElementTuple('fire', '1', 'aqua', 'wood'),
    'invisible': ElementTuple('invisible', '4', '', ''),
    'null': ElementTuple('null', '1', '', ''),
    'obstacle': ElementTuple('obstacle', '4', '', ''),
    'plus': ElementTuple('plus', '4', '', ''),
    'recovery': ElementTuple('recovery', '4', '', ''),
    'sword': ElementTuple('sword', '4', 'breaking', 'wind'),
    'terrain': ElementTuple('terrain', '4', '', ''),
    'wind': ElementTuple('wind', '4', 'sword', 'cursor'),
    'wood': ElementTuple('wood', '1', 'fire', 'electric')
}
elements = OrderedDict(sorted(elements.items()))

rarities = {
    1: 'common',
    2: 'uncommon',
    3: 'special',
    4: 'rare',
    5: 'very rare'
}
