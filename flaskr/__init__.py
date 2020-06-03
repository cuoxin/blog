import os

from flask import Flask, render_template, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile("config.py", silent=True)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = ""

@app.route("/")
def home():
    return render_template("home.html", theme="严泽旭")

@app.route("/aboutMe")
def aboutMe():
    return render_template("about_me.html", theme="关于我和本站")

@app.route("/contact")
def contact():
    return render_template("contact.html", theme="联系方式")

@app.route("/favicon.ico")
def favicon():
    return current_app.send_static_file('img/favicon.ico')

from flaskr import note, artical, error, backstage, login, set_password, search_label