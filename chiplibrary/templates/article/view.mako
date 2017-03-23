<%inherit file="../base.mako"/>
<%namespace name="functions" file="../widget/functions.mako"/>

<%def name="title()">Articles: ${article.name}</%def>
<%def name="title_breadcrumb()">${article.name}</%def>

<div class="article">
    <div class="meta">
        <div class="avatar">${functions.gravatar(article.author, size=50)}</div>
        <div class="written-by">Written by ${functions.user_link(article.author)} on <span class="date">${h.date(article.posted)}</span></div>
    </div>

    <div class="text">${article.content | h.markdown}</div>
</div>

<h3>Comments (${len(list(article.comments))})</h3>

% if article.comments:
<div class="comments">
    % for comment in article.comments:
        <div class="comment" id="comment-${comment.id}">
            <div class="written-by"><span class="author">${functions.user_link(comment.author)}</span> on <span class="date">${h.date(comment.posted)}</span> said:</p>
            ${comment.content | h.markdown}
        </div>
    % endfor
</div>
% else:
<p>No comments yet.</p>
% endif

<h3>Post a comment</h3>
% if request.user:
<form action="${request.current_route_path()}" class="comment-add" method="post">
    <p>Posting a comment as ${functions.user_link(request.user)}.  <a href="https://daringfireball.net/projects/markdown/syntax" title="Markdown Tutorial">Markdown</a> syntax is supported.</p>

    <p>${comment_form.comment}</p>
    <p>${comment_form.submit}</p>
</form>
% else:
<p>You must be logged in to comment.</p>
% endif

