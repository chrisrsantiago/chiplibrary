<%inherit file="base.mako"/>
<%def name="title()">Home</%def>

<div class="illustration illustration-home"></div>
<p>Welcome.  This is a battle chip index for the <strong>Mega Man Battle Network</strong> series.</p>

<p>To get started, type in the battlechip you are looking for, or simply browse through the index.  If you do not quite know what this is, the <a href="${request.route_path('about')}" title="About">about</a> should shed more light on what this is all about.</p>

<div class="clear"></div>
<h2>Latest Updates</h2>
<ul>
    <li><strong>10/01/16</strong>: Thanks to Tterraj42 and cheeseandcereal, Japanese names are available for a select few chips.</li>
    <li><strong>9/28/16</strong>: <a href="${request.route_path(route_name='search_index')}" title="Search">Search feature</a> has been re-done, and an advanced search functionality is also available to help further narrow searches.</li>
    <li><strong>9/27/16</strong>: Revamped site layout.</li>
</ul>
