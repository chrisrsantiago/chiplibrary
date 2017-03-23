<%inherit file="../base.mako"/>
<%def name="title()">Search</%def>

<%def name="render_field(field, linebreak=True)">
    % if linebreak:
        <p><label for="${field.name}" title="${field.description}">${field.label.text}</label><br>${field}</p>
    % else:
        <p><label for="${field.name}" title="${field.description}">${field.label.text}</label></p>
        ${field}
    % endif
</%def>

% if not request.GET or not results:
    <h2>Advanced Search</h2>
    <div class="advanced-search">
        <form action="${request.route_path('search')}" method="get">
            <p>All search fields that are not filled in are ignored, and all searches are case-insensitive.</p>

            <div class="column">
                <h3>Essential</h3>
                ${render_field(form.name)}
                ${render_field(form.name_jp)}
                <h3>Game Information</h3>
                ${render_field(form.game, linebreak=False)}
                ${render_field(form.version, linebreak=False)}
            </div>

            <div class="column">
                ${render_field(form.indice, linebreak=False)}
                ${render_field(form.indice_game, linebreak=False)}
                ${render_field(form.size, linebreak=False)}
                ${render_field(form.classification, linebreak=False)}
                ${render_field(form.element, linebreak=False)}
                ${render_field(form.code, linebreak=False)}
            </div>

            <div class="column">
            <h3>Damage Control</h3>
                <p>${form.damage_min(placeholder='Minimum')} | ${form.damage_max(placeholder='Maximum')}</p>
                <p>${form.recovery(placeholder='Recovery')}</p>
            <h3>Other</h3>
            ${render_field(form.rarity, linebreak=False)}
            </div>

            ${form.search_advanced}
            <div class="submit">${form.submit}</div>
        </form>
    </div>

    <h2>Search Mechanics</h2>
    <p>If you prefer to use the search box up top, here are a few pointers:</p>
    <div class="syntax-search">
        <dl>
            <dt>Searchable Attributes</dt>
            <dd>
                <ul>
                    <li>Names: <span class="syntax">name</span>, <span class="syntax">name_jp</span></li>
                    <li>Indices: <span class="syntax">indice</span>, <span class="syntax">indice_game</span></li>
                    <li>Game: <span class="syntax">game</span> (bn1, bn2, bn3, etc.)</li>
                    <li>Version: <span class="syntax">version</span> (white, blue, redsun, bluemoon, falzar, doubleteam, etc.)</li>
                    <li>Classification: <span class="syntax">classification</span> (standard, mega, giga, secret, dark, etc.)</li>
                    <li>Element: <span class="syntax">element</span> aqua, null, recovery, etc. (<a href="${request.route_url('elements')}" title="Elements">elements list</a>)</li>
                    <li>Code: <span class="syntax">code</span> A, B, C, *
                        <ul>
                            <li>For multiple chip codes, a comma-separated list can be used: A,B,C</li>
                        </ul>
                    </li>
                    <li>Rarity: <span class="syntax">rarity</span> 1, 2, 3, 4, 5</li>
                    <li>Size (MB): <span class="syntax">size</span> 22, 99, etc.</li>
                    <li>Damage: <span class="syntax">damage_min</span>, <span class="syntax">damage_max</span> and <span class="syntax">recovery</span>
                        <ul>
                            <li>Mathematical operations are also supported.</li>
                        </ul>
                    </li>
                </ul>
            </dd>
        </dl>
    </div>

    <% return STOP_RENDERING %>
% endif


% if results:
    <%include file="_results.mako"/>
% endif
