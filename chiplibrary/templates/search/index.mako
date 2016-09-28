<%inherit file="../base.mako"/>
<%def name="title()">Search</%def>

% if not request.GET or not results: 
    <h2>Advanced Search</h2>
    <div class="advanced-search">
        <form action="${request.route_path('search_index')}" method="get">
            <p>Using the advanced search, you can narrow your search query down further.  If you need help using the advanced search tools, you can always click the blue question marks for more information.</p>

            <p>All searches are case-insensitive.</p>
            
            % for field in form:
            <div class="description ${field.name}" title="${field.name.replace('_', ' ') | str.title}">
                ${field.description}
            </div>
            % endfor
            <div class="column">
            <h3>Essential</h3>
            % for field in form:
                % if field.name in ('name'):
                    <p>${field.label} <a class="help ${field.name}">Help</a> <br> ${field} </p>
                % endif
            % endfor
            <h3>Game Information</h3>
            % for field in form:
                % if field.name in ('game', 'version'):
                     <p>${field.label.text} <a class="help ${field.name}">Help</a></p>
                     ${field}
                % endif
            % endfor
            </div>
            
            <div class="column">
                % for field in form:
                    % if field.name in ('size', 'classification', 'element'):
                    <p>${field.label.text} <a class="help ${field.name}">Help</a></p>
                    ${field}
                    % endif
                % endfor
            </div>

            <div class="column">
            <h3>Damage Control</h3>
            % for field in form:
                % if field.name in ('damage_min', 'damage_max', 'recovery'):
                     <p>${field.label.text} <a class="help ${field.name}">Help</a></p>
                     ${field}
                % endif
            % endfor
            
            <h3>Other</h3>
            % for field in form:
                % if field.name in ('rarity'):
                     <p>${field.label.text} <a class="help ${field.name}">Help</a></p>
                     ${field}
                % endif
            % endfor
            </div>
            
            ${form.search_advanced}
            <div class="submit">${form.submit}</div>
        </form>
    </div>
   
    <h2><a name="search-syntax">Search Syntax</a></h2>
        <p>If you're an advanced user, you may use the following search syntax if using the search bar at top of the page:</p>
    <div class="syntax-search">
        <dl>
            <dt>Attribute Search</dt>
            <dd>You can search attributes as well, which is as simple as, <span class="syntax">game:bn4</span>.  Search supports the use of multiple attributes as well, so if you wanted to search for battlechips from BN4 with a specific chip code, <span class="syntax">game:bn4 code:a</span>, or even a list of chip codes, <span class="syntax">game:bn4 code:(a d)</span>.
            </dd>
            
            <dt>Search Operators</dt>
            <dd>Search operators
                <ul>
                    <li>AND &mdash; &amp;</li>
                    <li>OR &mdash; |</li>
                    <li>AND NOT &mdash; &!</li>
                    <li>AND MAYBE &mdash; &~</li>
                    <li>NOT &mdash; -</li>
                </ul>
            </dd>
        </dl>
    </div>
    
    <% return STOP_RENDERING %>
% endif


% if results:
    <%include file="_results.mako"/>
% endif
