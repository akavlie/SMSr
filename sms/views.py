import json

from sms import app
from flask import render_template, request, redirect, url_for, flash
from model import db, Sent, Message

from tw_send import twilio_send

@app.route('/')
def index():
    sent_messages = Sent.query.order_by(Sent.id.desc()).all()
    return render_template('index.html', sent_messages=sent_messages)

@app.route('/sms', methods=['POST'])
def sms():
    # Send to Twilio
    tw_response = twilio_send(request.form['phone_number'], request.form['message'])

    # Convert JSON from Twilio to Python dict
    sms_data = json.loads(tw_response)
    
    # Commit to database
    sms = Sent(sms_data['to'], sms_data['body'], sms_data['status'])
    db.session.add(sms)
    db.session.commit()

    # flash('SMS sent to %s' % request.form['phone_number'])
    return render_template('sent_message.html', sms=sms_data)
