$(document).ready(function() {
    // Use jQuery-UI's .autocomplete() to suggest search terms.
    $(function() { 
        $('.search-query').autocomplete({
            source: '/autocomplete',
            minLength: 2,
            select: function(event, ui) {
                // Redirect a user to the chip page if one is selected:
                if (ui.item){
                    urlparams = ui.item.value.split(':');
                    name = urlparams[0];
                    game = urlparams[1];
                    window.location.replace('/chips/' + game + '/' + name);
                }
            }
        });

        /*
            Format autocomplete search results with an icon and game name, so
            the user knows where to look.
        */
        $('.search-query').data('ui-autocomplete')._renderItem = function(ul, item) {
            var $img = $('<img>');
            var $li = $('<li>');
            
            $img.attr({src: item.icon, alt: item.label, width: '30', height: '30'});
            $li.attr('data-value', item.label);
            $li.append('<a href="#">');
            $li.find('a').append($img).append(item.label).append('<br><span class="game">' + item.game + '</span>');

            return $li.appendTo(ul);
          };
    });
    
    // Search Form
    $('a.help').click(function() {
        var classes = $(this).attr('class').split(' ');
        for (i = 0; i < classes.length; i++) {
            if (classes[i] !== 'help') {
                $('.description.' + classes[i]).dialog();
            }
        }
    });
});
