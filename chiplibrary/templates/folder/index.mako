<%inherit file="../base.mako"/>

<%def name="title()">Folders: Battle Network ${request.matchdict['game']}</%def>
<%def name="title_breadcrumb()">Folders</%def>

% if not folders:
    <p>There are no folders right now...Go ahead and submit one!</p>
    <% return STOP_RENDERING %>
% endif
<dl>
    % for folder in folders:
    <dd><a href="${request.route_path('folder_view', name=folder.slug)}" title="${folder.title}">${folder.title}</a> by ${folder.author.name}</dd>
    <dt>${folder.description}</dd>
    % endfor
</dl>
