from functools import wraps
from flask import Flask, render_template, request, session, redirect, url_for, flash, g
from db import connect as connection# connect importing connectin
from forms import URLForm, FileForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# from config.py file
app.config.from_object('config')
orm = SQLAlchemy(app)
from models import Location


@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])
def index():
	return render_template('index.html')


@app.route("/API/submit",methods = ['GET', 'POST'])
def submit():
	error=None
	form = URLForm(request.form)
	print("url submitted : " ,form.q.data)
	if(request.method == "GET"):
		return render_template("page.html", form=form)
	elif request.method == "POST" and form.validate():
		# print("url submitted : " ,form.q.data)
		inp(form.q.data)
	else:
		error="WRONG URL!!!"
	return render_template("page.html", form=form, error = error)

@app.route("/API/file",methods = ['GET', 'POST'])
def fsubmit():
	error=None
	form = FileForm(request.form)
	if request.method == "POST":
		print(form.validate())
		print("file submitted : " ,form.file)
		print("name: ", request.files["file"])
		# print("url submitted : " ,form.q.data)
		print(request.files["file"].filename)
		inp(request.files["file"].filename)
	elif(request.method=="POST"):
		error="WRONG FILE!!!"
	else:
		return render_template("uploader.html", form=form)
	return render_template("uploader.html", form=form, error = error)