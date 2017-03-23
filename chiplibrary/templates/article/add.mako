<%inherit file="../base.mako"/>

<%def name="title()">Adding Article for Battle Network ${request.matchdict['game']}</%def>
<%def name="title_breadcrumb()">Add</%def>

<form class="article-add" action="${request.route_path('article_add', game=request.matchdict['game'])}" method="post">
% for field in form:
    % if not field.name == 'submit':
    <p><label for="${field.name}" title="${field.description}">${field.label}</label></p>
    <p>${field}</p>
    % else:
        <p>${field}</p>
    % endif
% endfor
</form>
