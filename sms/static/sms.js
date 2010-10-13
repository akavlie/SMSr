var status_checker = 0;

$(function() {

  $('#test').click(function() {
      //$(".sent_message").css("background-color", "#FFFF9C")
       // .animate({ backgroundColor: "#FFFFFF", color: '#ffffff'}, 1500);
       $('.sent_message, .status').effect('highlight', {color: '#ffffff'}, 1500);

    });
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
            status_checker = setInterval('checkStatus()', 5000);
        }
    });
    return false;
  });

  // Plugin to enable placeholder text in form fields
  $('input:text, textarea').placeholder();

  // Highlight row for user when checked
  $('#db_users input').click(function() {
    if($(this).attr('checked')) {
      $(this).closest('tr').addClass('highlight');
    } else {
      $(this).closest('tr').removeClass('highlight');
    }
  });

  // Rows should remain highlighted after page refresh
  $('#db_users input:checked').closest('tr').addClass('highlight');



  // Not concerned with new user addition right now.
  /*  $('#new_user').submit(function() {
      $.post($SCRIPT_ROOT + '/user', $('#user_form').serialize() 
        function(data) {
        });
      return false;
    });
   */   
    // Plugin for placeholder text

});

function checkStatus() {
  // Check every message on the page with status "queued" or "sending" --
  // Twilio's status possibilities for unsent messsages
  $($('.queued, .sending').get().reverse()).each(function() {
    var sid = $(this).find('.sid').html();
    var status = $(this).children('.status').html();
    // Update status based on check with twilio
    $(this).children('.status').load($SCRIPT_ROOT + '/sms/update/' + sid, function(data) {
      // Add class based on current status; remove former status class 
      if(data != status) {
        $(this).parent().fadeOut();
        $(this).parent().removeClass('queued sending')
          .addClass(data)
          .fadeIn();
      }
        //.children('.sent_message, .status').effect('highlight', {color: '#ffffff'}, 3000);
    });
  });

  // Stop checking message status if there aren't any left
  if($('.queued, .sending').length == 0) {
    clearInterval(status_checker);
    status_checker = 0;
  }
}

