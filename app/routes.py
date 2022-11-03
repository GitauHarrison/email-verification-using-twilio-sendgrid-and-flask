from app import app
from flask import render_template, url_for, redirect, session
from app.forms import EmailForm, VerifyForm
from app.verify_email import request_email_verification_token, \
    check_email_verification_token


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = EmailForm()
    if form.validate_on_submit():
        user_email = form.email.data
        request_email_verification_token(user_email)
        session['email'] = user_email
        return redirect(url_for('verify_token'))
    return render_template('index.html', form=form)


@app.route('/verify-token', methods=['GET', 'POST'])
def verify_token():
    form = VerifyForm()
    if form.validate_on_submit():
        user_email = session['email']
        check_email_verification_token(user_email, form.token.data)
        return redirect(url_for('index'))
    return render_template('verify_token.html', form=form, title='Verify Token')
