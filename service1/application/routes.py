from flask import request, Response, render_template
import requests
from application import app, db
import random
from application.models import email

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

# Getting Email from Service
@app.route('/')
@app.route('/generate',methods=['GET'])
def generate():
    # Response request
    response_name = requests.get('http://service2:5001/get_name')
	response_number = requests.get('http://service3:5002/get_number')
    
    emailname = response_name.text+response_number.text
	email = requests.post('http://service4:5003/get_email',data=emailname)

    #   commiting response to database
    db_email = email(gen_email=response_email.text)
    db.session.add(db_email)
    db.session.commit()

    return render_template('generate.html',title='Your Email',data=response_email.txt)