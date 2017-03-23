<%inherit file="../base.mako"/>
<%def name="title()">Battle Network ${request.matchdict['game']}</%def>
<%def name="meta_description()">Extensive information on battlechips and folder strategies for Mega Man Battle Network ${request.matchdict['game']}</%def>

<div class="illustration illustration-bn${request.matchdict['game']}"></div>

<dl>
##    <dt><a href="${request.route_path('article_index', game=request.matchdict['game'])}" title="Articles: Battle Network ${request.matchdict['game']}">Articles</a></dt>
##    <dd>NetBattling articles written for ${self.title()}</dd>
    
    <dt><a href="${request.route_path('chip_index', game=request.matchdict['game'])}" title="Chips: Battle Network ${request.matchdict['game']}">Chips</a></dt>
    <dd>View the complete battle chip list for ${self.title()}</dd>

##    <dt><a href="${request.route_path('folder_index', game=request.matchdict['game'])}" title="Folders: Battle Network ${request.matchdict['game']}">Folders</a></dt>
##    <dd>A collection of compiled folders for ${self.title()} over the years from players of the metagame.</dd>
</dl>
