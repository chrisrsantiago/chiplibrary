# -*- coding: utf-8 -*-
"""Helper Functions and Variables"""

import mistune
import munch
from webhelpers2.html.tools import highlight

__all__ = [
    'highlight',
    'markdown',
    'chipimg',
    'weaknesses',
    'strengths',
    'rarities'
]

md_renderer = mistune.Renderer(escape=True, hard_wrap=True)
markdown = mistune.Markdown(renderer=md_renderer)

def chipimg(chip, request):
    """Returns an image filename for the given battlechip using the given
    Chip and Pyramid request objects.
    """
    if (isinstance(chip, dict)):
        chip = munch.munchify(chip)

    try:
        version = chip.version.name
    except AttributeError:
        version = ''

    if chip.classification.name == 'secret':
        classification = 'z'
    else:
        classification = chip.classification.name[:1]
    
    filename = u''.join([classification, str(chip.indice), version])
    
    return request.static_path(
        'chiplibrary:static/images/chips/%s/%s.gif' % (chip.game.name, filename)
    )
    
# Element weaknesses.
weaknesses = {
    'aqua'      : 'electric',
    'breaking'  : 'cursor',
    'cursor'    : 'wind',
    'electric'  : 'wood',
    'fire'      : 'aqua',
    'sword'     : 'breaking',
    'wind'      : 'sword',
    'wood'      : 'fire'
}

strengths = {v: k for k, v in weaknesses.items()}

rarities = {
    1: 'common',
    2: 'uncommon',
    3: 'special',
    4: 'rare',
    5: 'very rare'
}
