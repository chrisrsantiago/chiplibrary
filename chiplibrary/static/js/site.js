$(document).ready(function() {
    /*
        Search
    */
    // Use jQuery-UI's .autocomplete() to suggest search terms.
    $('.search-query').autocomplete({
        source: '/autocomplete',
        minLength: 2,
        select: function(event, ui) {
            // Redirect a user to the chip page if one is selected:
            if (ui.item){
                urlparams = ui.item.value.split(':');
                name = urlparams[0];
                game = urlparams[1];
                window.location.replace('/' + game + '/chips/' + name);
            }
        }
    }).data('ui-autocomplete')._renderItem = function(ul, item) {
        // Format autocomplete search results with an icon and game name, so
        // the user knows where to look.
        var $img = $('<img>');
        var $li = $('<li>');

        $img.attr({src: item.icon, alt: item.label, width: '30', height: '30'});
        $li.attr('data-value', item.label);
        $li.append('<a href="#">');
        $li.find('a').append($img).append(item.label).append('<br><span class="game">' + item.game + '</span>');

        return $li.appendTo(ul);
    };

    /*
        Login
    */
    login_dialog = $('div.login-modal').dialog({
      autoOpen: false,
      height: 400,
      width: 350,
      modal: true,
      buttons: {
        Cancel: function() {
          login_dialog.dialog('close');
        }
      }
    });

    $('div.userbar a.login').click(function() {
        login_dialog.dialog('open');
    });
    /*
        Mobile Functionality
    */
    $('div.mobile-menulink a.menu').sidr({
        name: 'sidr-left',
        side: 'left',
        method: 'toggle'
    });
    
    $('div.mobile-menulink a.search').click(function() {
        $(this).hide(); // We won't be needing this anymore.
        $('div.heading div.search').appendTo('div.mobile-menulink');
        $('input.search-query').focus();
    });
});
