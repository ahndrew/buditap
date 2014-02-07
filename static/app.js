$(function() {
    var BV = new $.BigVideo();
    BV.init();
    BV.show('/static/video/80s-Commercial-Strohs-Beer.mp4',{ambient:true});

    $('.btn').on('click',makeCall);

    function makeCall(e){
      e.preventDefault();
      var href, msg, cb,
          selected_theme = $('#theme_picker').find(":selected").val();

      if (e.target.id === "submit_theme") {
        if (selected_theme === 'choose theme') { 
          $('#theme_status').text('please choose a theme')
          return false;
        }
        href = e.target.href + selected_theme;
        cb = function(data){
          $('#theme_status').text('current theme: '+ data)
        }
      } else {
        href = e.target.href;
        cb = function(data){
          $('#status').text(data);
          $('#status').show();
        }
      }

      $.ajax({
        'type': 'GET',
        'url': href,
        success: function(data) {
          cb(data);
        },
        error: function(data) {
          $('#status').text('an error occured, refresh the page');
        }
      });
    }
});