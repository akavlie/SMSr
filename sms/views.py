from datetime import datetime
import json

from sms import app
from flask import render_template, request, redirect, url_for, flash
from model import db, User, SentMessage, FrequentText
from jinja2 import Environment

from tw_send import twilio_send, twilio_update


@app.route('/')
def index():
    sent_messages = SentMessage.query.order_by(SentMessage.id.desc())[0:10]
    users = User.query.order_by(User.first_name).all()
    return render_template('index.html', sent_messages=sent_messages,
                           users=users)

@app.route('/sms', methods=['POST'])
def sms():
    """Send an SMS to Twilio and save response to DB. """

    phone_numbers = request.form.getlist('user_phone')

    e = Environment()
    template = ''

    for p in phone_numbers:

        # Render Jinja2 template from message
        u = User.query.filter(User.phone == p).one()
        msg_template = e.from_string(request.form['message'])
        message = msg_template.render(first_name=u.first_name,
                                      last_name=u.last_name, phone=p)

        # Send to Twilio
        tw_response = twilio_send(p, message)

        # Convert JSON from Twilio to Python dict
        sms_data = json.loads(tw_response)
        #sms_data = {'to': 1234567899, 'body': 'Fake SMS', 'status': 'fake'}
        
        # Commit to database
        sms = SentMessage(sms_data['to'], sms_data['body'], sms_data['status'],
                          sms_data['sid'], datetime.now())
        db.session.add(sms)
        template += render_template('new_message.html', message=sms)

    db.session.commit()

    return template

@app.route('/sms/update/<sid>')
def sms_update(sid):
    """Update an SMS based on query from Twilio. """

    tw_response = twilio_update(sid)
    sms_data = json.loads(tw_response)

    sms = SentMessage.query.filter_by(sid=sid).one()
    sms.status = sms_data['status']
    db.session.commit()

    return sms.status

@app.route('/user')
def user_add():
    """Add a user to the DB. """

    u = User(request.form['user_name'], request.form['user_phone'])
    db.session.add(u)
    db.session.commit()

    users = User.query.all()

    return render_template('user.html', users=users)

