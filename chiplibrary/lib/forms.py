# -*- coding: utf-8 -*-
import string

from wtforms import (
    HiddenField,
    IntegerField,
    SelectField,
    SelectMultipleField,
    StringField
)
from wtforms import Form, SubmitField, validators, widgets

from . import reference

def form_errors(form):
    """Collect form errors and return the error messages as a list."""
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            error_messages.append('%s: %s' % (
                getattr(form, field).label.text,
                error
            ))
    return error_messages

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()
        
class ArticleForm(Form):
    name = StringField(
        'Name',
        description='''The name of your article.''',
        validators=[validators.DataRequired()]
    )
    description = StringField(
        'Description',
        description='''A brief description of the article and its
        intentions.''',
        validators=[validators.DataRequired()]
    )
    content = StringField(
        'Content',
        description='''The article itself.  Markdown formatting is
        allowed.''',
        validators=[validators.DataRequired()],
        widget=widgets.TextArea()
    )
    submit = SubmitField('Submit')

class CommentForm(Form):
    comment = StringField(
        'Comment',
        description='''Your actual comment.''',
        validators=[validators.DataRequired()],
        widget=widgets.TextArea()
    )
    submit = SubmitField('Submit')

class SearchForm(Form):
    indice = StringField(
        'Indice',
        description='''The chip indice.  This is the number that appears
        when viewing the game in the chip library.''',
        validators=[
            validators.optional()
        ]
    )
    indice_game = IntegerField(
        'Indice (Game)',
        description='''The in-game chip indice.  This is NOT the same as the
        regular chip indice.  This data is more for development/meta purposes.
        ''',
        validators=[
            validators.optional()
        ]
    )
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
    name_jp = StringField(
        'Name (Japanese)',
        description='''The chip name (Japanese).''',
        validators=[
            validators.optional(),
            validators.Length(
                min=2,
                message='''Chip name (Japanese) must be at least %(min)d
                characters.'''
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
        choices=[(code, code) for code in sorted(reference.chipcodes)],
        description='Chip codes for chip, ranging from A-Z and wildcard (*).',
        validators=[validators.optional()]
    )
    search_advanced = HiddenField(default='true')
    submit = SubmitField('Search')
