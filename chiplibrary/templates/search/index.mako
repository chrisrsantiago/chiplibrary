<%inherit file="../base.mako"/>
<%def name="title()">Search</%def>
<%def name="title_header()">Search: ${query}</%def>

% if form.errors:
    <div class="errors">
        <ul>
            % for k, v in form.errors.items():
            <li>${v[0]}</li>
            % endfor
        </ul>
    </div>
    <% return STOP_RENDERING %>
% endif

% if results:
<p>Found <strong>${len(results)} results</strong>:</p>
<ul>
% for chip in results:
    <li><img src="${h.chipimg(chip, request)}" alt="${chip['name']}"><a href="${request.route_path('chip_view_game', game=chip['game'].value, name=chip['name'])}" title="${chip['description']}">${chip['name']} &mdash; ${chip['game'].name}</a></li>
% endfor
</ul>
% else:
    <div class="errors">
        <ul>
            <li>No results found.</li>
        </ul>
    </div>
% endif
