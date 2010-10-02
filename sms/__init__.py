from flask import Flask

app = Flask(__name__)
app.config.from_object('sms.config')

import sms.views
