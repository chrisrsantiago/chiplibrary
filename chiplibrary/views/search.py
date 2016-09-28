# -*- coding: utf-8 -*-
from pyramid.view import view_config

from ..lib.helpers import chipimg
from ..lib.forms import SearchForm

@view_config(
    route_name='search_index',
    renderer='../templates/search/index.mako'
)
def index(request):
    form = SearchForm(request.GET)
    if request.GET:
        results = []

        if form.validate():
            search_params = []
            
            if form.name.data:
                # Since this view shares the same code as the top search bar,
                # it's important that we don't limit the query too much by
                # default unless the user
                if form.search_advanced.data:
                    search_params.append('name:%s' % (form.name.data))
                else:
                    search_params.append('%s' % (form.name.data))

            if form.classification.data:
                search_params.append(
                   'classification:(%s)' % 
                   (' '.join([form.classification.data]))
                )

            if form.game.data:
                search_params.append(
                    'game:(%s)' % (' '.join(form.game.data))
                )

            if form.damage_min.data:
                search_params.append(
                    'damage_min:%s' % (form.damage_min.data)
                )

            if form.damage_max.data:
                search_params.append(
                    'damage_max:%s' % (form.damage_max.data)
                )
                
            if form.recovery.data:
                search_params.append(
                    'recovery:%s' % (form.recovery.data)
                )

            if form.code.data:
                search_params.append(
                    'code:%s' % (form.code.data)
                )
                
            if form.element.data:
                search_params.append(
                   'element:(%s)' % (' '.join(form.element.data))
                )

            if form.size.data:
                search_params.append(
                    'size:%s' % (form.size.data)
                )

            if form.version.data:
                search_params.append(
                   'version:%s' % (' '.join(form.version.data))
                )

            # Attempt to put together a search query.
            query = ' '.join(search_params)
            lookup = request.library.lookup(query)
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
            else:
                error_message = 'Your search returned no results.'
                
                if len(search_params) > 4:
                    error_message = '''%s Try broadening your search and using
                    less specific parameters.''' % (error_message,)
                request.session.flash(error_message, 'errors')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    error_message = '%s: %s' % (
                        getattr(form, field).label.text,
                        error
                    )
                    request.session.flash(error_message, 'errors')
        return {'form': form, 'query': '', 'results': results}
    else:
        return {'form': form}

@view_config(route_name='search_autocomplete', renderer='json')
def autocomplete(request):
    """JSON representation of all battlechips, for use with autocomplete.
    """
    results = []
    try:
        term = request.GET['term']
        lookup = request.library.lookup(
            term,
            limit=request.library.SUGGESTIONS_LIMIT
        )
        
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
                'value': '%s:%s' % (
                    result['name_display'],
                    result['game']
                ),
                'game': result['game'].upper(),
                'icon': icon,
                'url': request.route_path(
                    'chip_view',
                    name=result['name_display'],
                    game=result['game'].lower()
                )
            })

    except (KeyError, NoResultFound):
        pass
    return results
