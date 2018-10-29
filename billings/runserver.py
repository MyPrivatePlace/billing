# -*- coding:utf-8 -*-

from billing import  app

@app.route('/')
def billinglogin():
    return  'Welcome to use billing system'

if __name__ == '__main__':
    app.run(debug = True)
