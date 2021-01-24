#basic modules for routes
from flask import Flask, redirect, url_for, send_file, render_template, flash, request, abort, send_from_directory
import schoolopy

#app instance
from app import app

#more schoolopy
from schoolopyInfo import schoolopyAuth, schoolopyUrl

#mail
from eMail import eMail

#index
@app.route('/', methods=["GET", "POST"])
def index():
    return "add me to the hangout again i didn't get it"

#login
@app.route('/login')
def home():
    print(schoolopyUrl)
    return redirect(schoolopyUrl)

#success
@app.route('/authorized')
def authorized():
    if not schoolopyAuth.authorize():
        return('hio')
    sc = schoolopy.Schoology(schoolopyAuth)
    me=sc.get_me()
    address=me.primary_email
    eml=eMail()
    eml.recipients=[address]
    eml.head="Your info"
    eml.body=str(me)
    eml.send()
    return render_template('authorized.html', person=me)


#sending an email
'''
@app.route('/email')
def sendEmail():
    eml=eMail()
    eml.recipients=["25aarushv@students.harker.org"]
    eml.head="Hello"
    eml.body="HELLOS"
    eml.send()
    return "success"
'''