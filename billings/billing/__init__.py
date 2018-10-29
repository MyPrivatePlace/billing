# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create project object
app = Flask(__name__)

#import os
#print os.environ.keys()
#print os.environ.get('FLASKR_SETTING')
#load config file
app.config.from_object('billing.setting')
app.config.from_envvar('FLASKR_SETTINGS')

# create db object
db = SQLAlchemy(app)