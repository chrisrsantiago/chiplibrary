<%inherit file="../base.mako"/>

<%def name="title()">Folders: ${folder.name}</%def>
<%def name="title_breadcrumb()">${folder.name}</%def>

<div class="folder">
    <div class="description">${folder.description}</div>

    <h2>Chips</h2>
    <ul class="chips">
        % for chip in folder.chips:
        <li><a href="${request.route_path('chip_view', game=folder.game[2:])" title="${chip.name}">${chip.name}</a> ${chip.chip_code}</li>
        % endfor
    </ul>

    <h2>Summary</h2>
    {folder.summary | h.markdown}
</div>

<h2>Comments (${len(article.comments)})</h2>
<div class="comments">
% if article.comments:
    % for comment in article.comments:
        <div class="comment">
            <p>Posted by <strong>${functions.user_link(comment.author)}</strong> on ${h.date(article.comment.posted)}</p>
            ${comment.content | h.markdown}
        </div>
    % endfor
% else:
    <p>No comments yet.</p>
% endif
</div>
