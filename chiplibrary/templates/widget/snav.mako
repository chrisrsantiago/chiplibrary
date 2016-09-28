<%
    request_uri = request.environ['PATH_INFO']
%>

% if request_uri == request.route_path('search_index'):
    <li><a href="${request.route_path('search_index')}">Help</a></li>
% elif any(s in request_uri for s in ('bn1', 'bn2', 'bn3', 'bn4', 'bn5', 'bn6', 'elements')):
    <li><a href="${request.route_path('search_index')}">Search</a></li>
    <li><a href="${request.route_path('element_index')}" title="Elements">Elements</a></li>
% else:
    <li><a href="${request.route_path('about')}">About</a></li>
    <li><a href="${request.route_path('credits')}">Credits</a></li>
    <li><a href="${request.route_path('search_index')}">Search</a></li>
    <li><a href="http://github.com/chrisrsantiago/chiplibrary">Development and Bugs</a></li>
% endif
