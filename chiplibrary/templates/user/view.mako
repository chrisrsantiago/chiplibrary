<%inherit file="../base.mako"/>
<%namespace name="functions" file="../widget/functions.mako"/>

<%def name="title()">Users: ${user.username}</%def>
<%def name="title_header()">
    ${user.username}
</%def>
<%def name="title_breadcrumb()">${user.username}</%def>

<p>${functions.gravatar(user)}</p>

<h2>Contributions</h2>

<h3>Folders</h3>
% if user.folders:
    <ul>
    % for folder in user.folders:
        <li><a href="${request.route_path('folder_view', name=folder.slug, game=folder.game.value)}">${folder.name}</a> &mdash; ${folder.game.name}</li>
    % endfor
    </ul>
% else:
    <p>No folders.</p>
% endif

<h3>Articles</h3>
% if user.articles:
    <ul>
    % for article in user.articles:
        <li><a href="${request.route_path('article_view', id=article.id, game=article.game.value)}">${article.name}</a> &mdash; ${article.game.name}</li>
    % endfor
    </ul>
% else:
    <p>No articles.</p>
% endif
