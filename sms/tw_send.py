from sms import app
import twilio

def twilio_send(phone_number, message):
    """Sends an SMS via the Twilio service. """

    data = {'From': app.config['CALLER_ID'], 
            'To': phone_number, 
            'Body': message}

    account = twilio.Account(app.config['ACCOUNT_SID'],
                             app.config['ACCOUNT_TOKEN'])

    tw_response = account.request('/%s/Accounts/%s/SMS/Messages.json' % 
                               (app.config['API_VERSION'], app.config['ACCOUNT_SID']),
                               'POST', data)

    return tw_response

def twilio_update(sid):
    """Update status for a given SMS. """

    account = twilio.Account(app.config['ACCOUNT_SID'],
                             app.config['ACCOUNT_TOKEN'])

    tw_response = account.request('/%s/Accounts/%s/SMS/Messages/%s.json' % 
                                  (app.config['API_VERSION'],
                                   app.config['ACCOUNT_SID'], sid),
                                  'GET')

    return tw_response
