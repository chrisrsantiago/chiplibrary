# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators

class SearchForm(Form):
    q = StringField(u'Search Term',
        validators=[
            validators.input_required('You must type in a search query.'),
            validators.Length(
                min=2,
                message='Your search query is not specific enough.'
            )
        ]
    )
