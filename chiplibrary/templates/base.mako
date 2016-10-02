<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">

    <meta name="description" content="${self.meta_description() | str.strip}">

    <link rel="self" type="application/opensearchdescription+xml" title="Chip Library" href="${request.static_path('chiplibrary:static/opensearch.xml')}">
    
    <link rel="apple-touch-icon" sizes="57x57" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-57x57.png')}">
    <link rel="apple-touch-icon" sizes="60x60" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-60x60.png')}">
    <link rel="apple-touch-icon" sizes="72x72" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-72x72.png')}">
    <link rel="apple-touch-icon" sizes="76x76" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-76x76.png')}">
    <link rel="apple-touch-icon" sizes="114x114" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-114x114.png')}">
    <link rel="apple-touch-icon" sizes="120x120" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-120x120.png')}">
    <link rel="apple-touch-icon" sizes="144x144" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-144x144.png')}">
    <link rel="apple-touch-icon" sizes="152x152" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-152x152.png')}">
    <link rel="apple-touch-icon" sizes="180x180" href="${request.static_path('chiplibrary:static/images/site/icons/apple-icon-180x180.png')}">
    <link rel="icon" type="image/png" sizes="192x192"  href="${request.static_path('chiplibrary:static/images/site/icons/android-icon-192x192.png')}">
    <link rel="icon" type="image/png" sizes="32x32" href="${request.static_path('chiplibrary:static/images/site/icons/favicon-32x32.png')}">
    <link rel="icon" type="image/png" sizes="96x96" href="${request.static_path('chiplibrary:static/images/site/icons/favicon-96x96.png')}">
    <link rel="icon" type="image/png" sizes="16x16" href="${request.static_path('chiplibrary:static/images/site/icons/favicon-16x16.png')}">

    <link rel="manifest" href="${request.static_path('chiplibrary:static/images/site/icons/manifest.json')}">
    
    <title>${self.title()} | chiplibrary</title>

    % for stylesheet in ('global', 'chip', 'search', 'jquery/jquery-ui'):
    <link href="${request.static_path('chiplibrary:static/css/%s.css' % (stylesheet,))}" rel="stylesheet">
    % endfor
      
    % for script in ('jquery-3.0.0.min', 'jquery-ui.min', 'search'):
    <script src="${request.static_path('chiplibrary:static/js/%s.js' % (script,))}" type="text/javascript"></script>
    % endfor
    
    <%include file="widget/meta.mako"/>
</head>
<body>
<div class="fixed">
    <div class="nav">
        <ul>
            <li class="home"><a title="Home" href="${request.route_path('index')}">Home</a></li>
            % for game in (1, 2, 3, 4, 5, 6):
                <% selected = '' %>
                % if ''.join(['bn', str(game)]) in request.environ['PATH_INFO']:
                    <% selected = ' selected' %>
                % endif
            <li class="bn${game}${selected}"><a title="Battle Network ${game}" href="${request.route_path('chip_index_game', game=game)}">BN${game}</a></li>
            % endfor
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
    % if request.session.peek_flash('errors'):
    <div class="errors">
        <ul>
            % for error in request.session.pop_flash('errors'):
                <li>${error}</li>
            % endfor
        </ul>
    </div>
    % endif
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
${self.body()}
    <div class="footer">Copyright &copy; Chris Santiago.  Mega Man is a registered trademark of Capcom.</div> 
</div> 
</body>
</html>
<%def name="title_header()">${self.title()}</%def>
<%def name="title_breadcrumb()">${self.title()}</%def>
<%def name="meta_description()">A comprehensive battlechip reference for the Mega Man Battle Network series.</%def>
