<%namespace name="functions" file="functions.mako"/>
<div class="userbar">
    % if request.user:
    <p>Hello, <a href="${request.route_path('user_my')}" title="View your profile">${request.user.username}</a> (<a href="${request.route_path('user_logout')}?next=${request.path}" title="Logout">Logout</a>)</p>
    % else:
    <p>Hello, Guest (<a href="#" class="login" title="Login/Register">Login</a>)</p>
    % endif
</div>
