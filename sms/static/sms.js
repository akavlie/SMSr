var status_checker = 0;

$("#sms_form").submit(function() {
  // Post form data via AJAX
  $.post($SCRIPT_ROOT + "/sms", $("#sms_form").serialize(),
      function(data) {
          // Insert returned HTML after the heading
          $('#sent_message_list h2').after(data);
          // Animate height expansion, then opacity
          $('.new').animate({height: 'toggle'})
              .animate({opacity: 1})
              // Remove class so it doesn't catch animation again
              .removeClass('new');
          // Check status of new messages at set interval
          if(status_checker==0) {
              status_checker = setInterval('checkStatus()', 5000);
          }
      });
    return false;
});

function checkStatus() {
  // Check every message on the page with status "queued" or "sending" --
  // Twilio's status possibilities for unsent messsages
  $('.queued, .sending').children('.status').each(function(i) {
    var sid = $(this).parent().find('.sid').html();
    // Update status based on check with twilio
    $(this).load($SCRIPT_ROOT + '/sms/update/' + sid, function(status) {
      // Add class based on current status; remove former status class 
      $(this).parent().addClass(status).removeClass('queued sending');
    });
  });
  // Stop checking message status
  clearInterval(status_checker);
  status_checker = 0;
}

