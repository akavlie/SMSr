# SMSr

SMSr is a simple [Flask](http://flask.pocoo.org/)-based web application for
sending SMS messages to mobile phones. It uses the 
[Twilio](http://www.twilio.com/) API.


## Requirements

- Python 2.5+
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy/)
- A [Twilio](http://www.twilio.com/) account


## Installation

1. Make a copy of `config.py.example` to `config.py` within the `/sms` subdirectory.
1. Enter your Twilio account SID, token, and caller ID in `config.py`.
1. Choose one of the deployment options in the 
   [Flask documentation](http://flask.pocoo.org/docs/deploying/) 
   if deploying to a server. It should be a standard Flask setup, as long as
   the Flask, SQLAlchemy, and Flask-SQLAlchemy dependencies are met.
