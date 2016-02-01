from app import app
from flask import render_template
import os

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/cam')
def cam():
	return render_template('cam.html')
