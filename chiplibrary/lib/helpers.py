# -*- coding: utf-8 -*-
"""Helper Functions"""
import re
import urllib.parse
import hashlib
from collections import namedtuple

import inflect
import mistune
import munch
from webhelpers2.text import truncate
from webhelpers2.html.builder import literal
from webhelpers2.html.tools import highlight
from romkan import to_roma

__all__ = [
    'chipimg',
    'date',
    'favicon',
    'gravatar',
    'highlight',
    'literal',
    'markdown',
    'normalize_slug',
    'pluralizer',
    'to_roma',
    'truncate'
]

md_renderer = mistune.Renderer(escape=True, hard_wrap=True)
md_parser = mistune.Markdown(renderer=md_renderer)
pluralizer = inflect.engine()

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

    filename = ''.join([classification, str(chip.indice), version])

    return request.static_path(
        'chiplibrary:static/images/chips/%s/%s.gif' % (chip.game.name, filename)
    )

def date(dt):
    """Take a datetime.datetime object and return a formatted string with an
    appropriate representation."""
    return dt.strftime('%b %d, %Y @ %I:%M%p')
    
def favicon():
    """Generate a favicon list, and differentiate between apple icons and
    regular favicons.
    
    Returns a list containing a NamedTuple with the following 
    string attributes.
        
        `resolution`
            Ex. 16x16, 32x32
        `prefix`
            'favicon' or 'apple-icon-'
        `rel`
            'icon' or 'apple-touch-icon'
    """
    resolutions = set([16, 32, 96, 192, 57, 60, 72, 76, 114, 120, 144, 152, 180])
    Icon = namedtuple('Icon', 'resolution, prefix, rel')
    icons = []

    for resolution in resolutions:
        if resolution in set([16, 32, 96]):
            prefix = 'favicon-'
            rel = 'icon'
        else:
            prefix = 'apple-icon-'
            rel = 'apple-touch-icon'

        icons.append(Icon(
            '%sx%s' % (resolution, resolution),
            prefix,
            rel
        ))
    return icons

def gravatar(email, size=100):
    """Generate a Gravatar URL with the given email address."""
    default = 'identicon'

    email = hashlib.md5(email.encode('utf-8').lower()).hexdigest()
    options = urllib.parse.urlencode({'d': default, 's': str(size)})

    gravatar_url = 'https://www.gravatar.com/avatar/%s?%s' % (email, options)

    return gravatar_url

def markdown(text):
    """Parses a given string using Markdown."""
    return literal(md_parser(text))

def normalize_slug(slug):
    """Creates a pretty URL representation of the article name.
    
    `slug`
        The desired string to convert to a slug.

    Returns a string with the following modifications:
        ~ Whitespace stripped from start/end
        ~ Double and single-quotes removed, to stop the awkward dash in
        contractions.
        ~ Non-alphanumeric characters (including spaces) converted into
        dashes (-)
        ~ Lowercased string
    """
    slug = slug.strip()
    slug = slug.replace("'", '').replace('"', '')
    slug = slug.lower()
    slug = re.sub(r'\W+', '-', slug)
    return slug
