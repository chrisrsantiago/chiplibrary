<%inherit file="../base.mako"/>

<%def name="title()">User List</%def>
<%def name="title_breadcrumb()">Users</%def>

% if users:
    <ul>
    % for user in users:
        <li><a href="${request.route_path('user_view', id=user.id)}" title="${user.username}'s Profile">${user.username}</a></li>
    % endfor
    </ul>
% else:
    <p>No users to list.</p>
% endif
