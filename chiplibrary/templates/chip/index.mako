<%inherit file="../base.mako"/>
<%def name="title()">Chips: Battle Network ${request.matchdict['game']}</%def>
<%def name="title_breadcrumb()">Chips</%def>

<table class="battlechips">
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
        <col class="rarity">
        % if settings['classifications']:
        <col class="classification">
        % endif
    </colgroup>
    <tbody>
    <tr>
        <th class="indice">#</th>
        <th></th>
        <th class="name">Name</th>
        <th class="element">Element</th>
        <th class="damage">Damage</th>
        <th class="recovery">Recovery</th>
        <th class="codes">Code(s)</th>
        % if settings['size']:
        <th class="size">Size</th>
        % endif
        <th class="rarity">Rarity</th>
        % if settings['classifications']:
        <th class="classifications">Classification</th>
        % endif
    </tr>
        % for chip in chips:
        <tr>
            <td class="indice">${chip.indice}</td>
            <td class="image"><img src="${h.chipimg(chip, request)}" alt="${chip.name}"></td>
            <td class="name"><a href="${request.route_path('chip_view', game=chip.game.value, name=chip.name)}">${chip.name}</a>
            </td>
            <td class="element"><a href="${request.route_path('search', _query={'element': chip.element.name})}" title="${chip.element.name | str.title}"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (chip.element.name))}" alt="${chip.element.name}"></a></td>
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
            <td class="codes">
            % for code in chip.codes_iter():
                <%
                    comma = ', '
                    if loop.last:
                        comma = ''
                %>
                <a href="${request.route_path('search', _query={'code': code, 'game': chip.game.name})}" title="Chips with code ${code} for ${chip.game.name | str.upper}">${code}</a>${comma}
            % endfor
            </td>
            % if settings['size']:
            <td class="size">${chip.size}MB</td>
            % endif
            <td class="rarity"><a href="${request.route_path('search', _query={'rarity': chip.rarity, 'game': chip.game.name})}" title="Chips with rarity of ${chip.rarity}">${'*' * chip.rarity}</td>
            % if settings['classifications']:
            <td class="classifications"><a href="${request.route_path('search', _query={'classification': chip.classification.name, 'game': chip.game.name})}" title="Search for ${chip.classification.name} chips"><span class="${chip.classification.name | str.lower}">${chip.classification.name}</span></a></td>
            % endif
        </tr>
        % endfor
    </tbody>
</table>
