function MagicNumberEditXBlock(runtime, element) {
    $(element).find('.save-button').bind('click', function(e) {
      e.preventDefault();
      var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
      var data = {
        number: $(element).find('input[name=number]').val()
      };

      runtime.notify('save', {state: 'start'});
      $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
        $('.magic-number', element).text(response.number);
        runtime.notify('save', {state: 'end'});
        runtime.notify('cancel', {});
      });
    });

    $(element).find('.cancel-button').bind('click', function() {
      runtime.notify('cancel', {});
    });
}
