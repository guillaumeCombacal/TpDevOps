#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "This is a Flask app created with Vagrant & Ansible!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #same host & port use with gunicorn in ansible-flask > default
