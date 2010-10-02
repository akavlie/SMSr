from sms import app
from flask import render_template, request, redirect, url_for, flash
from model import db, Sent, Message

from tw_send import twilio_send

@app.route('/')
def index():
    sent_messages = Sent.query.all()
    return render_template('index.html', sent_messages=sent_messages)

@app.route('/sms', methods=['POST'])
def sms():
    twilio_send(request.form['phone_number'], request.form['message'])
    sms = Sent(request.form['phone_number'], request.form['message'])
    db.session.add(sms)
    db.session.commit()

    flash('SMS sent to %s' % request.form['phone_number'])
    return redirect(url_for('index'))
