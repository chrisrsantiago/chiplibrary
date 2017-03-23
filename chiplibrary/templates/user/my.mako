<%inherit file="../base.mako"/>
<%namespace name="functions" file="../widget/functions.mako"/>
<%def name="title()">Control Panel</%def>

<p>You may adjust your user settings on here.</p>

<h2>Profile Settings</h2>

<h3>Username</h3>
<p>Your current username is <strong>${request.user.username}</strong>.</p>

<h3>Email</h3>
% if request.user.email:
<p>Your email address is <strong>${request.user.email}</strong>.</p>
% else:
<p>You do not have an email on file.</p>
% endif

<h3>Gravatar</h3>
<p>${functions.gravatar(request.user)}</p>
<p>We use Gravatar for user avatars.  If you do not or you already have a Gravatar, using the same email address associated with this account, you may <a href="http://gravatar.com/" title="Gravatar">update it</a> on their website and it will update here as well.</p>

<h2>Social Accounts</h2>
<p>So far, your account is associated with the following login providers.  You may associate your account with additional login providers, or disconnect them from your account.  By associating your account with more login providers, you may login to your account from multiple sites.</p>

% for assoc in social['backends']['associated']:
<form action="${request.route_url('social.disconnect_association', backend=assoc.provider, association_id=assoc.id)}" method="post" class="clearfix">
    <input id="_csrf" type="hidden" value="${request.session.get_csrf_token()}"/>
    <ul class="login-providers">
        <li class="${assoc.provider.title() | str.lower}"><a>${assoc.provider.title()}</a>
            <li><button>Disconnect</button></li>
    </ul>
</form>
% endfor

<div class="clear"></div>
<h3>Add</h3>
<ul class="login-providers">
    % for name in social['backends']['not_associated']:
    <li class="${name}"><a href="${request.route_url('social.auth', backend=name)}" title="${name | str.title}">${name}</a></li>
    % endfor
</ul>
