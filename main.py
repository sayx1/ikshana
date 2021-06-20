''' imports 
		create_app for app init '''
from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
import os
import re

'''pandas'''
import pandas as pd;
from pandas import DataFrame, read_csv;
path = os.getcwd()+'/to_do/log.txt'
fhandle = open(path)
text = fhandle.read()
lines = text.split("\n")
result =[]
for line in lines:
	pieces = [p for p in re.split("( |\\\".*?\\\"|'.*?')", line[1:-1]) if p.strip()]
	if len(pieces) == 10:
		ip = pieces[0]
		date = pieces[3]
		request = pieces[5]
		webbrowser = pieces[9]
	result.append([ip,date,request,webbrowser])
df = pd.DataFrame(result, columns=['ip', 'date', 'request','webbrowser'])
table_ren = df.describe()


''' main blue print '''
main = Blueprint('main',__name__)


''' paths '''
@main.route('/') # base home page
def index():
	return render_template('index.html')

''' profile '''
@main.route('/profile') # profile page that you get after logging in
@login_required
def profile():
	return render_template('profile.html', name=current_user.name, tables=[table_ren.to_html(classes='data')], titles=["na"])

