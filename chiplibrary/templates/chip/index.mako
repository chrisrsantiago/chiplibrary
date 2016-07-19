<%inherit file="../base.mako"/>

% if not 'game' in request.matchdict:
    <p>You need to pick a game bro.</p>
% elif not result:
    <p>No results found.</p>
    <% return '' %>
% endif

<table class="battlechips sortable">
<thead>
    <tr>
        <th>Indice</th>
        <th>Name</th>
        <th>Element</th>
        <th>Damage</th>
        <th>Recovery</th>
        <th>Code(s)</th>
        <th>Size</th>
        <th>Classification</th>
    </tr>
</thead>
<tbody>
% for chip in result:
<tr>
    <td>${h.attribute(chip.indices).indice}</td>
    <td><a href="${request.route_url('chip_view_game', game=request.matchdict['game'], name=h.attribute(chip.names).name)}">
        <img src="${request.static_url('chiplibrary:static/images/chips/bn%s/%s.gif' % (request.matchdict['game'], h.attribute(chip.indices).indice))}" alt=""><br>${h.attribute(chip.names).name}</a>
    </td>
    <td><a href="#" title="${h.attribute(chip.elements).element.name}"><img src="${request.static_url('chiplibrary:static/images/elements/%s.png' % (h.attribute(chip.elements).element.name))}" alt="${h.attribute(chip.elements).element.name}"></a></td>
    <td>${h.attribute(chip.powers).damage}</td>
    <td>${h.attribute(chip.powers).recovery}</td>
    <td>${h.attribute(chip.codes, True)}</td>
    <td>${h.attribute(chip.sizes).size}MB</td>
    <td>${h.attribute(chip.classifications).classification.name}</td>
</tr>
% endfor
</tbody>
</table>
