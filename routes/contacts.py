from flask import Blueprint, redirect, render_template, url_for, flash, request
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.get('/')
def home():
    contacts_data = Contact.query.all()

    return render_template('index.html', contacts=contacts_data)


@contacts.route('/new', methods=['POST'])
def add_contact():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(username, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added successfully")

    return redirect(url_for('contacts.home'))


@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contact_data = Contact.query.get(id)
    if request.method == 'POST':
        contact_data.username = request.form['username']
        contact_data.phone = request.form['phone']
        contact_data.email = request.form['email']
        db.session.commit()

        flash("Contact updated successfully")

        return redirect(url_for('contacts.home'))

    return render_template('update.html', contact=contact_data)


@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()

    flash("Contact deleted successfully")

    return redirect(url_for('contacts.home'))
