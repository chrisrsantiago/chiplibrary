<%inherit file="../base.mako"/>

<%def name="title()">Elements</%def>
<%def name="title_header()">Elements</%def>

<table class="battlechips sortable">
    <colgroup>
        <col class="indice">
        <col class="name">
        <col class="introduced-in">
        <col class="weakness">
        <col class="strength">
    </colgroup>
    <tbody>
        <tr>
            <th></th>
            <th>Name</th>
            <th>Introduced In</th>
            <th>Weak Against (2x)</th>
            <th>Strong Against (2x)</th>
        </tr>
        % for key, element in r.elements.items():
        <tr>
            <td class="indice"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (element.name,))}" alt="${element.name}"></td>
            <td><a href="${request.route_path('search', _query={'element': element.name})}" title="Search for chips with element: ${element.name | str.title}">${element.name}</a></td>
            <td><a href="${request.route_path('game', game=element.introduced)}" title="Battle Network ${element.introduced.replace('bn', '')}">Battle Network ${element.introduced.replace('bn', '')}</a></td>
            <td>
                % if element.weakness:
                <img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (element.weakness,))}" alt="${element.weakness}">
                % else:
                N/A
                % endif
            </td>
            <td>
                % if element.strength:
                <img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (element.strength,))}" alt="${element.strength}">
                % else:
                N/A
                % endif
            </td>
        </tr>
        % endfor
    </tbody>
</table>
