<%inherit file="../base.mako"/>

<%def name="title()">Battle Network ${chip.game.value} &mdash; ${chip.name}</%def>
<%def name="title_header()">${chip.name}</%def>

<div class="chip-view">
    <div class="left ${chip.classification.name | str.lower}">
    <div class="image"><img src="${request.static_path('chiplibrary:static/images/chips/%s/%s.gif' % (chip.game.name, h.chipimg(chip)))}" alt="${chip.name}"></div>
    <dl>
        <dt>Codes</dt>
        <dd>
            <ul>
            % for code in chip.codes:
                <li>${code.code}</li>
            % endfor
            </ul>
        </dd>
        % if chip.damage_min:
        <dt>Damage</dt>
        <dd class="damage">${chip.damage_min}</dd>
        % endif
        % if chip.recovery:
        <dt>Recovery</dt>
        <dd class="recovery">${chip.recovery}</dd>
        % endif
        <dt>Elemental Information</dt>
        <dd>This is a <a href="${request.route_path('element_view', name=chip.element.name)}" title="${chip.element.name}"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (chip.element.name))}" alt="${chip.element.name}"> (${chip.element.name | str.title})</a>  chip.
        % if not chip.element.name == 'null':
        It is strong against <a href="${request.route_path('element_view', name=h.strengths[chip.element.name])}" title="${h.strengths[chip.element.name]}"><img src="${request.static_path('chiplibrary:static/images/elements/%s.png' % (h.strengths[chip.element.name]))}" alt="${h.strengths[chip.element.name]}"> (${h.strengths[chip.element.name]})</a>-based opponents.
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
            <dt>Game</dt>
            <dd><a href="${request.route_path('chip_index_game', game=chip.game.value)}">Battle Network ${chip.game.value}</a></dd>
            <dt>Rarity</dt>
            <dd>This is a <strong>${h.rarities[chip.rarity]}</strong> chip.</dd>
            % if chip.version:
            <dt>Version</dt>
            <dd>${chip.version.name | str.title}</dd>
            % endif
            % if not chip.game in ('bn1', 'bn2'):
            <dt>Classification</dt>
            <dd class="${chip.classification.name}">${chip.classification.name | str.title}</dd>
            % endif
            <dt>Description (in-game)</dt>
             <dd>${chip.description}</dd>
            <dt>Summary</h3>
            % if chip.summary:
            <dd>${chip.summary | h.markdown}</dd>
            % else:
            <dd>No summary available.</dd>
            % endif
        </dl>
    </div>
</div>
