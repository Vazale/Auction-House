from ext import db, Login_Manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class BaseModel:
    def Create(self):
        db.session.add(self)
        db.session.commit()

    def Delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def Save():
        db.session.commit()
class Product(db.Model, BaseModel):

    __tablename__ = "Products"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    img = db.Column(db.String(), default="example.png")
    desc = db.Column(db.String())

class Profile(db.Model, BaseModel, UserMixin):

    __tablename__ = "Profiles"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    mail = db.Column(db.String())
    profile_img = db.Column(db.String(),default="static/images/pfp images/profile.jpg")

    
    def __init__(self, username, password, mail):
        self.username = username
        self.password = generate_password_hash(password)
        self.mail = mail


    def check_password(self, password):
        return check_password_hash(self.password, password)
        


@Login_Manager.user_loader
def load_user(user_id):
    return Profile.query.get(user_id)