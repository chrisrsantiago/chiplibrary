<p>Found <strong>${len(results)} results</strong>:</p>

<ul>
% for chip in results:
    <li><img src="${h.chipimg(chip, request)}" alt="${chip['name']}"><a href="${request.route_path('chip_view_game', game=chip['game'].value, name=chip['name'])}" title="${chip['description']}">${chip['name']} &mdash; ${chip['game'].name}</a></li>
% endfor
</ul>
