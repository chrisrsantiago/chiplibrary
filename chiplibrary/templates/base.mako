<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="icon" href="${request.static_url('chiplibrary:static/favicon.png')}">

    <title>chiplibrary - ${title}</title>
    
    <link href="${request.static_url('chiplibrary:static/css/global.css')}" rel="stylesheet">
    <link href="${request.static_url('chiplibrary:static/css/tables.css')}" rel="stylesheet">
</head>
<body>

<div id="header"><a href="${request.route_url('index')}">chiplibrary</a></div>
<div id="nav">
    <ul>
        <li id="home"><a title="Home" href="${request.route_url('index')}">Home</a></li>
        % for game in [1, 2, 3, 4, 5, 6]:
        <li id="bn${game}"><a title="Battle Network ${game}" href="${request.route_url('chip_index_game', game=game)}">BN${game}</a></li>
        % endfor
    </ul>
</div>
<ul id="snav">
    <li><a href="${request.route_url('index')}">Home</a></li>
    <li><a href="${request.route_url('about')}">About</a></li>
    <li><a href="${request.route_url('credits')}">Credits</a></li>
    ##todo: login system
    ##<li><a href="${request.route_url('user_preferences')}">Preferences</a></li>
    ##<li><a href="${request.route_url('user_login')}">Login/Register</a></li>
    <li><a href="http://github.com/chrisrsantiago/chiplibrary">Development and Bugs</a></li>
</ul>
<div id="content">
    <h1>${title}</h1>
${self.body()}
    <br style="clear: both;" />
</div> 
<div id="footer">Copyright &copy; Chris Santiago.  Mega Man is a registered trademark of Capcom.</div> 
</body>
</html>
