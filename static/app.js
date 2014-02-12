$(function() {
    var BV = new $.BigVideo();
    BV.init();
    BV.show(['/static/video/80s-Commercial-Strohs-Beer.mp4','/static/video/tapper-arcade.mp4'],{ambient:true});

    $('.btn').on('click',makeCall);

    function makeCall(e){
      e.preventDefault();
      var selected_theme = $('#theme_picker').find(":selected").val();

      //defaults
      var href = e.target.href;
      var cb = function(data){
        $('#status').text(data).show();
      }

      switch (e.target.id) {
        case "change_vol":
          var level = $('#vol').val().trim();
          href += level
        break;

        case "submit_theme":
          if (selected_theme === 'choose theme') { 
            $('#theme_status').text('please choose a theme')
            return false;
          }
          href += selected_theme;
          cb = function(data){
            $('#theme_status').text('current theme: '+ data)
          }
        break;

        default:
          //do nothing different
        break;

      }

      $.ajax({
        'type': 'GET',
        'url': href,
        success: function(data) {
          cb(data);
        },
        error: function(data) {
          $('#status').text('an error occured, refresh the page').show();
        }
      });
    }
});