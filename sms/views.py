import json

from sms import app
from flask import render_template, request, redirect, url_for, flash
from model import db, User, SentMessage, FrequentText
from datetime import datetime

from tw_send import twilio_send

@app.route('/')
def index():
    sent_messages = SentMessage.query.order_by(SentMessage.id.desc()).all()
    return render_template('index.html', sent_messages=sent_messages)

@app.route('/sms', methods=['POST'])
def sms():
    """Send an SMS to Twilio and save response to DB. """

    # Send to Twilio
    tw_response = twilio_send(request.form['phone_number'], request.form['message'])

    # Convert JSON from Twilio to Python dict
    sms_data = json.loads(tw_response)
    #sms_data = {'to': 1234567899, 'body': 'Fake SMS', 'status': 'fake'}
    
    # Commit to database
    sms = SentMessage(sms_data['to'], sms_data['body'], sms_data['status'],
                      sms_data['sid'], datetime.now())
    db.session.add(sms)
    db.session.commit()

    # flash('SMS sent to %s' % request.form['phone_number'])
    return render_template('sent_message.html', sms=sms_data)

@app.route('/sms/update/<sid>', methods=['POST'])
def sms_update(sid):
    """Update an SMS based on query from Twilio. """

    tw_response = twilio_update(sid)
    sms_data = json.loads(tw_response)

    sms = SentMessage.query.filter_by('sid=%s' % sid).one()
    sms.status = sms_data.status
    db.session.commit()

    return sms_data.status


