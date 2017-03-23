<%inherit file="base.mako"/>
<%def name="title()">Home</%def>

<div class="illustration illustration-home"></div>
<p><strong>chiplibrary</strong> is a battle chip index for the <strong>Mega Man Battle Network</strong> series.  Aside from that, this is also a resource for information on the <abbr title="competitive play">metagame</abbr> aspect of the games.  If you are a competitive player yourself and are interested in sharing this knowledge, </p>

<p>To get started, type in the battlechip you are looking for, or simply browse through the index to find what you are looking for.  If you do not quite know what this is, the <a href="${request.route_path('about')}" title="About">about</a> should shed more light on what this is all about.</p>


<h2>Latest Updates</h2>
<p>This is the user-friendly version of most of the updates.  If you are looking for more technical information/updates, have a look at the <a href="http://github.com/chrisrsantiago/chiplibrary/" title="GitHub">GitHub</a> page.</p>

<ul>
    <li><strong>3/21/17</strong>: User accounts are now supported on the website, which will be convenient when it comes to submitting or editing content (articles, folders, etc.) on the website in an upcoming update.  In accomodation for these features, game pages no longer display battle chip lists by default, and as such all have been redirected so as to not break old URLs.  Stay tuned for further enhancements!</li>
    <li><strong>10/15/16</strong>: A mobile version of the website is now available, making it far more convenient to browse chiplibrary using mobile devices with smaller screens.</li>
    <li><strong>10/02/16</strong>: chiplibrary.net is now the official URL to accessing the website.  If you are using the old url (chips.nachtara.com,) your browser will automatically redirect you to the new website.</li>
</ul>
