from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, phone) -> None:
        self.username = username
        self.email = email
        self.phone = phone
