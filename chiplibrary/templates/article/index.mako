<%inherit file="../base.mako"/>
<%namespace name="functions" file="../widget/functions.mako"/>

<%def name="title()">Articles: Battle Network ${request.matchdict['game']}</%def>
<%def name="title_breadcrumb()">Articles</%def>

% if not articles:
    <p>There are no articles right now.  You can <a href="${request.route_path('article_add', game=request.matchdict['game'])}" title="Write an article">write one</a> if you would like :).</p>
    <% return STOP_RENDERING %>
% endif

<p><a href="${request.route_path('article_add', game=request.matchdict['game'])}" title="Write an article">Write an article</a></p>
<dl>
    % for article in articles:
    <dt><a href="${request.route_path('article_view', id=article.id, game=article.game.value)}" title="${article.name}">${article.name}</a> by ${functions.user_link(article.author)}</dt>
    <dd>${article.description}</dd>
    % endfor
</dl>
