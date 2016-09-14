<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    
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

    % for stylesheet in ('global.css', 'chip.css', 'jquery/jquery-ui.css'):
    <link href="${request.static_path('chiplibrary:static/css/%s' % (stylesheet,))}" rel="stylesheet">
    % endfor
      
    % for script in ('jquery-3.0.0.min.js', 'jquery-ui.min.js', 'search.js'):
    <script src="${request.static_path('chiplibrary:static/js/%s' % (script,))}" type="text/javascript"></script>
    % endfor
</head>
<body>

<div id="header"><a href="${request.route_path('index')}">chiplibrary</a></div>
<div id="nav">
    <ul>
        <li id="home"><a title="Home" href="${request.route_path('index')}">Home</a></li>
        % for game in [1, 2, 3, 4, 5, 6]:
        <li id="bn${game}"><a title="Battle Network ${game}" href="${request.route_path('chip_index_game', game=game)}">BN${game}</a></li>
        % endfor
    </ul>
</div>
<ul id="snav">
    <li><a href="${request.route_path('index')}">Home</a></li>
    <li><a href="${request.route_path('about')}">About</a></li>
    <li><a href="${request.route_path('credits')}">Credits</a></li>
    <li><a href="http://github.com/chrisrsantiago/chiplibrary">Development and Bugs</a></li>
</ul>
<div id="content">
    <%include file="widgets/search.mako"/>
    <div id="log"></div>
    <h1>${self.title_header()}</h1>
${self.body()}
    <br style="clear: both;" />
</div> 
<div id="footer">Copyright &copy; Chris Santiago.  Mega Man is a registered trademark of Capcom.</div> 
</body>
</html>
<%def name="title_header()">${self.title()}</%def>
