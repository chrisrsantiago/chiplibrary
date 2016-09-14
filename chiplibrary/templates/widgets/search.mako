<% q = '' %>

% if request.environ['PATH_INFO'] == request.route_path('search_index'):
    <% q = request.GET.get('q', '') %>
% endif
<div id="search">
    <form action="${request.route_path('search_index')}" method="get">
        <input id="search-query" name="q" type="text" value="${q}"><input type="submit" value="Search">
    </form>
</div>



