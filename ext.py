from flask import Flask, render_template, redirect
from flask_sqlalchemy import  SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "fabnny"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db = SQLAlchemy(app)
Login_Manager = LoginManager(app)

Login_Manager.login_view = "login"
