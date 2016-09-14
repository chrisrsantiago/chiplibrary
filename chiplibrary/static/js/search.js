$(document).ready(function() {

    $(function() { 
        $('#search-query').autocomplete({
            source: '/autocomplete',
            minLength: 2
        });
        
        $('#search-query').data('ui-autocomplete')._renderItem = function(ul, item) {
            var $img = $('<img>');
            var $li = $('<li>');
            
            $img.attr({src: item.icon, alt: item.label, width: '30', height: '30'});
            $li.attr('data-value', item.label);
            $li.append('<a href="#">');
            $li.find('a').append($img).append(item.label).append('<br><span class="game">' + item.game + '</span>');

            return $li.appendTo(ul);
          };
    });
});
