<%
    request_uri = request.path_info
    games = ['bn1', 'bn2', 'bn3', 'bn4', 'bn5', 'bn6']
%>

% if any(s in request_uri for s in set(games + ['element'])):
    % for game in games:
        % if game in request_uri:
            <% current_game = game[2:] %>
            <li><a href="${request.route_path('article_index', game=current_game)}" title="Articles for ${current_game | str.upper}">Articles</a></li>
            <li><a href="${request.route_path('chip_index', game=current_game)}" title="Chips for ${current_game | str.upper}">Chips</a></li>
            <li><a href="${request.route_path('folder_index', game=current_game)}" title="Folders for ${current_game | str.upper}">Folders</a></li>
        % endif
    % endfor
    <li><a href="${request.route_path('elements')}" title="Elements">Elements</a></li>
    <li><a href="${request.route_path('search')}" title="Search">Search</a></li>
% else:
    <li><a href="${request.route_path('about')}" title="About">About</a></li>
    <li><a href="${request.route_path('credits')}" title="Credits">Credits</a></li>
    <li><a href="${request.route_path('development')}" title="Development">Development</a></li>
% endif
