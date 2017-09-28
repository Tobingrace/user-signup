from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)


class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            flash('You are now registered and can log in', 'success')
            redirect(url_for('index'))
        else:
            flash('Please correct the issues below', 'danger')
            return render_template('register.html', form=form)
    
    return render_template('register.html', form=form)


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = "secretkey"
    app.run(debug=True)
