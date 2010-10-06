var status_checker = 0;

$(function() {
    $('#test').click(function() {
        $('.sent_message:first').slideToggle(1000);
    });

    $("#sms_form").submit(function() {
        // Post form data via AJAX
        $.post($SCRIPT_ROOT + "/sms", $("#sms_form").serialize(),
            function(data) {
                // Insert returned HTML before the first message
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

});

function checkStatus() {
    $('.queued, .sending, .fake').children('.status').each(function(i) {
            if ($(this).text() == 'fake') {
                $(this).html('TEST');
            } else {
                $(this).html('FAIL');
            }
            $(this).parent().removeClass('queued sending fake');
    });
    // Stop checking message status
    clearInterval(status_checker);
    status_checker = 0;
}

