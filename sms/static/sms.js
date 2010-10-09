var status_checker = 0;

$(function() {

  // SMS SUBMISION
  // -------------
  $("#sms_form").submit(function() {
    // Post form data via AJAX
    $.post($SCRIPT_ROOT + "/sms", $("#sms_form").serialize(),
      function(data) {
        // Insert returned HTML after the heading
        $('#sent_message_list h2').after(data);
        // Animate height expansion, then opacity
        $('.new').css({opacity: 0})
          .animate({height: 'toggle'})
          .animate({opacity: 1})
          // Remove class so it doesn't catch animation again
          .removeClass('new');
        // Check status of new messages at set interval
        if(status_checker==0) {
            status_checker = setInterval('checkStatus()', 3000);
        }
    });
    return false;
  });

/*  $('#new_user').submit(function() {
    $.post($SCRIPT_ROOT + '/user', $('#user_form').serialize() 
      function(data) {
      });
    return false;
  });
 */   
  // Plugin for placeholder text
  $('input:text').placeholder();

});

function checkStatus() {
  // Check every message on the page with status "queued" or "sending" --
  // Twilio's status possibilities for unsent messsages
  $('.queued, .sending').each(function(i) {
    var sid = $(this).find('.sid').html();
    // Update status based on check with twilio
    $(this).children('.status').load($SCRIPT_ROOT + '/sms/update/' + sid, function(status) {
      // Add class based on current status; remove former status class 
      $('.queued, .sending').addClass(status).removeClass('queued sending');
    });
  });

  // Stop checking message status if there aren't any left
  if($('.queued, .sending').length > 0) {
    clearInterval(status_checker);
    status_checker = 0;
  }
}

