from ext import app, db

from sql import Profile

with app.app_context():

    db.drop_all()

    db.create_all()
    admin = Profile(username="ADMIN", password="Thispasforad", mail="admin@mail.com")
    Profile.Create(admin)
    