$(function() {
    var BV = new $.BigVideo();
    BV.init();
    BV.show('/static/video/80s-Commercial-Strohs-Beer.mp4',{ambient:true});

    $('.btn').on('click',makeCall);

    function makeCall(e){
      e.preventDefault();

      $.ajax({
        'type': 'GET',
        'url': e.target.href,
        success: function(data) {
          $('#status').text(data);
          $('#status').show();
        },
        error: function(data) {
          $('#status').text('an error occured, refresh the page');
        }
      });
    }
});