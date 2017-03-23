<%def name="gravatar(usr, size=100)">
    <img src="${h.gravatar(usr.email, size)}" alt="${usr.username}">
</%def>

<%def name="nav()">
    <li class="home"><a title="Home" href="${request.route_path('index')}">Home</a></li>
    % for game in (1, 2, 3, 4, 5, 6):
        <% selected = '' %>
        % if ''.join(['bn', str(game)]) in request.environ['PATH_INFO']:
            <% selected = ' selected' %>
        % endif
    <li class="bn${game}${selected}"><a title="Battle Network ${game}" href="${request.route_path('game', game=game)}">BN${game}</a></li>
    % endfor
</%def>

<%def name="user_link(user)">
<a href="${request.route_path('user_view', id=user.id)}" title="View profile for ${user.username}">${user.username}</a>
</%def>
