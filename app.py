from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from configuration import SECRET_KEY, DATABASE_CONNECTION_URI
app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


app.register_blueprint(contacts)


if __name__ == '__main__':
    app.run(debug=True)
