<%inherit file="../base.mako"/>

<%def name="title()">
% if 'game' in request.matchdict:
    Chips: Battle Network ${request.matchdict['game']}
% else:
    Chips
% endif
</%def>

% if not 'game' in request.matchdict:
    <p>Pick a game!</p>
    % for game in range(1,7):
        <a href="${request.route_path('chip_index_game', game=game)}" title="Battle Network ${game}" class="noborder"><img src="${request.static_path('chiplibrary:static/images/titles/bn%s.gif' % (game,))}" alt="Battle Network ${game}"></a>
        % if game == 3:
            <br>
        % endif
    % endfor
    </ul>
    <% return STOP_RENDERING %>
% elif not chips:
    <p>No results found.</p>
    <% return STOP_RENDERING %>
% endif

<table class="battlechips sortable">
<colgroup>
    <col class="indice">
    <col class="image">
    <col class="name">
    <col class="element">
    <col class="damage">
    <col class="recovery">
    <col class="codes">
    % if settings['size']:
    <col class="size">
    % endif
    % if settings['classifications']:
    <col class="classification">
    % endif
</colgroup>
<tbody>
<tr>
    <th class="indice">#</th>
    <th></th>
    <th>Name</th>
    <th>Element</th>
    <th>Damage</th>
    <th>Recovery</th>
    <th>Code(s)</th>
    % if settings['size']:
    <th>Size</th>
    % endif
    % if settings['classifications']:
    <th>Classification</th>
    % endif
</tr>
% for chip in chips:
<tr>
    <td class="indice">${chip.indice}</td>
    <td><img src="${h.chipimg(chip, request)}" alt="${chip.name}"></td>
    <td><a href="${request.route_path('chip_view_game', game=chip.game.value, name=chip.name)}">${chip.name}</a>
    </td>
    <td><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (chip.element.name))}" alt="${chip.element.name}"></td>
    <td class="damage">
    % if chip.damage_min > 0:
        ${chip.damage_min}
    % elif chip.damage_min == -1:
        Variable
    % else:
        ????
    % endif
    % if chip.damage_max > chip.damage_min:
        &mdash;${chip.damage_max}
    % endif
    </td>
    <td class="recovery">
    % if chip.recovery:
        ${chip.recovery}
    % endif
    </td>
    <td>
    % for code in chip.codes_iter():
        <%
            comma = ', '
            if loop.last:
                comma = ''
        %>
        ${code}${comma}
    % endfor
    </td>
    % if settings['size']:
    <td>${chip.size}MB</td>
    % endif
    % if settings['classifications']:
    <td><span class="${chip.classification.name | str.lower}">${chip.classification.name}</span></td>
    % endif
</tr>
% endfor
</tbody>
</table>
