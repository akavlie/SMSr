from sms import app
from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Sent(db.Model):
    """ Record of a sent message """
    __tablename__ = 'sent_messages'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    date = db.Column(db.Date)
    message = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, phone, message, status):
        self.phone = phone
        self.message = message
        self.status = status

class Message(db.Model):
    """ Frequently used SMS messages """
    __tablename__ = 'frequent_smses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    message = db.Column(db.String)

