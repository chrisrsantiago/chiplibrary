<%inherit file="../base.mako"/>

<%def name="title()">Battle Network ${chip.game.value} &mdash; ${chip.name}</%def>
<%def name="title_breadcrumb()">${chip.name}</%def>
<%def name="title_header()">${chip.name}</%def>
<%def name="meta_description()">(${chip.game.name | str.upper}) ${chip.name} - ${chip.description}</%def>

<div class="chip-view">
    <div class="left ${chip.classification.name | str.lower}">
    <div class="image"><img src="${h.chipimg(chip, request)}" alt="${chip.name}"></div>

    <dl>
        <dt>Description (in-game)</dt>
        <dd>${chip.description}</dd>

        <dt>Game</dt>
        <dd><a href="${request.route_path('game', game=chip.game.value)}">Battle Network ${chip.game.value}</a></dd>

        % if not chip.game in ('bn1', 'bn2'):
        <dt>Classification</dt>
        <dd class="${chip.classification.name}">${chip.classification.name | str.title}</dd>
        % endif

        <dt>Codes</dt>
        <dd>
            <ul>
            % for code in chip.codes_iter():
                <li><a href="${request.route_path('search', _query={'game': chip.game.name, 'code': code})}" title="Chips with code ${code} for ${chip.game.name | str.upper}">${code}</a></li>
            % endfor
            </ul>
        </dd>
        % if chip.damage_min:
        <dt>Damage</dt>
        <dd class="damage">
            ${chip.damage_min}
            % if chip.damage_max > chip.damage_min:
            &mdash;%{chip.damage_max}
            % endif
        </dd>
        % endif

        % if chip.recovery:
        <dt>Recovery</dt>
        <dd class="recovery">${chip.recovery}</dd>
        % endif
        
        <dt>Elemental Information</dt>
        <dd>This is a <a href="${request.route_path('search', _query={'element': chip.element.name})}" title="${chip.element.name}"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (chip.element.name))}" alt="${chip.element.name}"> (${chip.element.name | str.title})</a> chip.
        % if r.elements[chip.element.name].strength:
        It is strong against <a href="${request.route_path('search', _query={'element': r.elements[chip.element.name].strength})}" title="${r.elements[chip.element.name].strength}"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (r.elements[chip.element.name].strength))}" alt="${r.elements[chip.element.name].strength}"> (${r.elements[chip.element.name].strength})</a>-based opponents.
        % else:
        It has no elemental strengths.
        % endif
        </dd>
        
        % if chip.effects:
        <dt>Chip Effects</dt>
        <dd>
            <ul>
                % if chip.effects.flinch:
                <li>This chip causes flinching</li>
                % endif
                % if chip.effects.timestop:
                <li>This chip stops time</li>
                % endif
                % if chip.effects.paralyze:
                <li>This chip causes paralysis</li>
                % endif
                % if chip.effects.push:
                <li>This chip pushes the player back</li>
                % endif
            </ul>
        </dd>
        % endif
    </dl>
    </div>
    
    <div class="extended right">
        <dl>
            <dt>Names</dt>
            <dd class="names">
                <ul>
                    <li class="en">English: ${chip.name}</li>
                    % if chip.name_jp:
                    <li class="jp">Japanese: ${chip.name_jp}</li>
                    <li class="jp">Romaji: ${h.to_roma(chip.name_jp)}</li>
                    % endif
                </ul>
            </dd>

            <dt>Indices</dt>
            <dd>
                <ul>
                    <li><abbr title="The number seen in the chip library">Library</abbr>: ${chip.indice}</li>
                    <li><abbr title="Development purposes">In-game</abbr>: ${chip.indice_game}</li>
                </ul>
            </dd>
            
            <dt>Rarity</dt>
            <dd><strong>${r.rarities[chip.rarity] | str.title}</strong> &mdash; ${chip.rarity} ${h.pluralizer.plural('star', chip.rarity)}</dd>

            % if othergames:
            <dt>Other Games</dt>
            <dd class="othergames">
                <ul>
                % for otherchip in othergames:
                <li><a href="${request.route_path('chip_view', name=otherchip.name, game=otherchip.game.value)}" title="${otherchip.name}"><img src="${h.chipimg(otherchip, request)}" alt=${otherchip.name}"> <span>${otherchip.name} (${otherchip.game.name})</span></a></li>
                % endfor
                </ul>
            </dd>
            % endif

            % if chip.version:
            <dt>Version</dt>
            <dd>${chip.version.name | str.title}</dd>
            % endif
            
            % if chip.summary:
            <dt>Summary</h3>
            <dd>${chip.summary | h.markdown}</dd>
            % endif
        </dl>
    </div>
</div>
