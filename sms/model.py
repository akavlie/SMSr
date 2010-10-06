from sms import app
from flaskext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    """Basic user record. """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    sent_messages = db.relationship('SentMessage',
                                    order_by='SentMessage.date',
                                    backref='user') 

class SentMessage(db.Model):
    """Record of a sent SMS message """
    __tablename__ = 'sent_messages'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    date = db.Column(db.Date)
    message = db.Column(db.String)
    status = db.Column(db.String)
    sid = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, phone, message, status, sid, date):
        self.phone = phone
        self.message = message
        self.status = status
        self.sid = sid
        self.date = date

class FrequentText(db.Model):
    """Frequently used SMS message """
    __tablename__ = 'frequent_smses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    message = db.Column(db.String)

