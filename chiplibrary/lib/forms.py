# -*- coding: utf-8 -*-
import string

from wtforms import (
    Form,
    HiddenField,
    IntegerField,
    StringField,
    SelectField,
    SelectMultipleField,
    SubmitField,
    validators,
    widgets
)
from wtforms.validators import ValidationError

from . import reference

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()

class SearchForm(Form):
    name = StringField(
        'Name',
        description='''The chip name.  All are case-insensitive, unless
        specified otherwise.''',
        validators=[
            validators.optional(),
            validators.Length(
                min=2,
                message='Chip name must be at least %(min)d characters.'
            )
        ]
    )
    classification = MultiCheckboxField(
        'Classification',
        choices=[(c.name, c.name.title()) for c in reference.Classification],
        description='''(BN3+ Only) Chip Classification.  Every chip has a
        classification, which is a ranking system in its own right in order to
        limit the number of those chips a user may have in their folder.''',
        validators=[validators.optional()]
    )
    game = MultiCheckboxField(
        'Game',
        choices=[(g.name, g.name.upper()) for g in reference.Game],
        description='''Self-explanatory.  Certain chips may apear in a game more
        than once, albeit with different attributes.  If you wish to search for
        a chip that may appear in specific games, you may do so.''',
        validators=[validators.optional()]
    )
    version = MultiCheckboxField(
        'Version',
        choices=[(v.name, v.name.title()) for v in reference.Version],
        description='''(BN3+ Only) The game version.  Certain chips are only
        available on certain versions of the game, either due to diferences
        in enemies or storyline.  By narrowing it down to versions, you get to
        see version-exclusive chip.''',
        validators=[validators.optional()]
    )
    element = MultiCheckboxField(
        'Element',
        choices=[(e.name, e.name.title()) for e in reference.Element],
        description='''Every chip has an element.  Certain elements are only
        available in certain games.''',
        validators=[validators.optional()]
    )
    rarity = MultiCheckboxField(
        'Rarity',
        choices=[(str(r), '%s' % (reference.rarities[r].title()))
            for r in range(1,6)
        ],
        description='Chip rarity, ranging from 1-5.',
        validators=[
            validators.optional()
        ],
    )
    damage_min = IntegerField(
        'Damage (Minimum)',
        description='Amount of minimum damage a chip inflicts.',
        validators=[
            validators.optional()
        ],
    )
    damage_max = IntegerField(
        'Damage (Maximum)',
        description='''Amount of maximum damage a chip inflicts.  For SP/DS
        navi chips and multi-hitting chips, this would reflect the total
        amount of damage inflicted, but it should be noted that support chips
        are not counted.''',
        validators=[
            validators.optional()
        ]
    )
    size = IntegerField(
        'Size (MB)',
        description='''(BN2+ Only) The regular memory requirement to be able
        to set the chip as a regular chip in-game.  Useful when one needs a
        chip to be readily available on battle start.''',
        validators=[
            validators.optional(),
            validators.NumberRange(min=1, max=99)
        ]
    )
    recovery = IntegerField(
        'Recovery',
        description='Amount of HP recovered from chip.',
        validators=[validators.optional()]
    )
    code = MultiCheckboxField(
        'Code',
        choices = [
            (code, code) for code in (list(string.ascii_uppercase) + ['*'])
        ],
        description='Chip codes for chip, ranging from A-Z and wildcard (*).',
        validators=[validators.optional()]
    )
    search_advanced = HiddenField(default='true')
    submit = SubmitField('Search')
