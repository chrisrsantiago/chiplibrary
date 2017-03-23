<%namespace name="functions" file="widget/functions.mako"/>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
    <meta name="description" content="${self.meta_description() | str.strip}">

    <link rel="self" type="application/opensearchdescription+xml" title="Chip Library" href="${request.static_path('chiplibrary:static/opensearch.xml')}">
    <link rel="manifest" href="${request.static_path('chiplibrary:static/images/site/icons/manifest.json')}">
    % for icon in h.favicon():
    <link rel="${icon.rel}" type="image/png" sizes="${icon.resolution}" href="${request.static_path('chiplibrary:static/images/site/icons/%s%s.png' % (icon.prefix, icon.resolution,))}">
    % endfor

    <title>${self.title()} | chiplibrary</title>

    <link href="${request.static_path('chiplibrary:static/style.css')}" rel="stylesheet">
    % for script in ('jquery-3.0.0.min', 'jquery-ui.min', 'jquery.sidr.min', 'site'):
    <script src="${request.static_path('chiplibrary:static/js/%s.js' % (script,))}" type="text/javascript"></script>
    % endfor

    <%include file="widget/meta.mako"/>
</head>
<body>
<div class="fixed">
    <%include file="widget/userbar.mako"/>
    <div class="mobile-menulink">
        <div class="button left"><a class="menu" href="#menu">Menu</a></div>
        <div class="button right"><a class="search" href="#search">Search</a></div>
    </div>

    <div class="nav">
        <ul>
        ${functions.nav()}
        </ul>
    </div>
    <ul class="snav">
    <%include file="widget/snav.mako"/>
    </ul>
</div>
<div class="heading">
    <div class="header">
    <%include file="widget/search.mako"/>
        <div class="logo"></div>
    </div>
</div>
<div class="content">
    <div class="breadcrumbs">
    % for bread in request.bread:
        % if bread['url']:
        <a href="${bread['url']}">${bread['title']}</a> &raquo;
        % else:
        <strong>${self.title_breadcrumb()}</strong>
        % endif
    % endfor
    </div>

    <h1>${self.title_header()}</h1>
    % if request.session.peek_flash('errors'):
    <div class="errors">
        <ul>
            % for error in request.session.pop_flash('errors'):
                <li>${error}</li>
            % endfor
        </ul>
    </div>
    % endif
${self.body()}
    <div class="footer">
        <p>Copyright &copy; <a href="http://nachtara.com/" title="Chris Santiago">Chris Santiago</a>.  Mega Man is a registered trademark of Capcom.
        <div class="affiliates">
            <a href="http://rockman-exe.com/"><img src="${request.static_path('chiplibrary:static/images/site/affiliates/rmexe.gif')}" alt="RockMan EXE"></a>&nbsp;
            <a href="http://www.therockmanexezone.com/" title="The Rockman EXE Zone"><img src="${request.static_path('chiplibrary:static/images/site/affiliates/trez.png')}" alt="The Rockman EXE Zone"></a>
        </div>
    </div>
</div>

<div id="sidr-left">
    <ul>
    ${functions.nav()}
    </ul>
</div>

% if not request.user:
<div class="login-modal">
<%include file="widget/login.mako"/>
</div>
% endif
</body>
</html>
<%def name="title_header()">${self.title()}</%def>
<%def name="title_breadcrumb()">${self.title()}</%def>
<%def name="meta_description()">A comprehensive battlechip reference for the Mega Man Battle Network series.</%def>
