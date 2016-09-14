# -*- coding: utf-8 -*-
from pyramid.view import view_config
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

from ..lib.helpers import chipimg
from ..lib.forms import SearchForm

@view_config(route_name='search_index', renderer='../templates/search/index.mako')
def index(request):
    form = SearchForm(request.GET)
    results = []

    if form.validate():
        lookup = request.library.lookup(form.q.data)
        if lookup:
            for result in lookup:
                results.append({
                    'indice': result['indice'],
                    'name': result['name_display'],
                    'game': result['game_enum'],
                    'classification': result['classification_enum'],
                    'version': result.get('version_enum', None),
                    'description': result['description']
                })
    return {'form': form, 'query': form.q.data, 'results': results}
    
@view_config(route_name='search_autocomplete', renderer='json')
def autocomplete(request):
    """JSON representation of all battlechips, for use with autocomplete.
    """
    results = []
    try:
        term = request.GET['term']
        lookup = request.library.lookup(term, prefix=True)
        
        if not lookup:
            return {}
            
        for result in lookup:
            icon = chipimg(
                {
                    'indice': result['indice'],
                    'name': result['name_display'],
                    'game': result['game_enum'],
                    'classification': result['classification_enum'],
                    'version': result.get('version_enum', None)
                },
                request
            )
            results.append({
                'id': result['indice'],
                'label': result['name_display'],
                'value': 'game:%s name:%s' % (
                    result['game'],
                    result['name_display']
                ),
                'game': result['game'].upper(),
                'icon': icon
            })

    except (NoResultFound):
        pass
    return results
