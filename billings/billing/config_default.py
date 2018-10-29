# -*- coding:utf-8 -*-
# config_default.py for development environment

#start DEBUG mode
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'db':{
        'host': 'sdp-dbs-dev2',
        'port': 3306,
        'user': 'sysadmin',
        'password': 'remote',
        'database': 'sdp_billing'
    },
    'session':{
        'secret':'DasiNiWeigou'
    }

}
