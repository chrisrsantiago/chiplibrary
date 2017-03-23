<p>Registration is quick and simple&mdash;creating an account allows you to post and comment on articles and folders.</p>

<ul class="login-providers">
    <li class="google-oauth2"><a href="${request.route_url('social.auth', backend='google-oauth2')}?next=${request.path}" title="Google">Google</a></li>
##    <li class="facebook-app"><a href="${request.route_url('social.auth', backend='facebook-app')}?next=${request.path}" title="Facebook">Facebook</a></li>
    <li class="flickr"><a href="${request.route_url('social.auth', backend='flickr')}?next=${request.path}" title="Flickr">Flickr</a></li>
    <li class="github"><a href="${request.route_url('social.auth', backend='github')}?next=${request.path}" title="Github">Github</a></li>
##<li class="instagram"><a href="${request.route_url('social.auth', backend='instagram')}?next=${request.path}" title="Instagram">Instagram</a></li>
    <li class="linkedin"><a href="${request.route_url('social.auth', backend='linkedin')}?next=${request.path}" title="LinkedIn">LinkedIn</a></li>
    <li class="reddit"><a href="${request.route_url('social.auth', backend='reddit')}?next=${request.path}" title="Reddit">Reddit</a></li>
    <li class="steam"><a href="${request.route_url('social.auth', backend='steam')}?next=${request.path}" title="Steam">Steam</a></li>
    <li class="twitter"><a href="${request.route_url('social.auth', backend='twitter')}?next=${request.path}" title="Twitter">Twitter</a></li>
    <li class="yahoo-oauth"><a href="${request.route_url('social.auth', backend='yahoo-oauth')}?next=${request.path}" title="Yahoo!">Yahoo!</a></li>
</ul>
