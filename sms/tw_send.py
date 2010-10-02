from sms import app
import twilio

def twilio_send(phone_number, message):
    """Sends an SMS via the Twilio service. """

    data = {'From': app.config['CALLER_ID'], 
            'To': phone_number, 
            'Body': message}

    account = twilio.Account(app.config['ACCOUNT_SID'],
                             app.config['ACCOUNT_TOKEN'])
    account.request('/%s/Accounts/%s/SMS/Messages' % (app.config['API_VERSION'],
                                                      app.config['ACCOUNT_SID']),
                    'POST', data)
