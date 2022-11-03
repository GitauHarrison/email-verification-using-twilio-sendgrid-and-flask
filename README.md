# Email Verification Using Twilio SendGrid

Twilio provides SendGrid that can be used for everything email. This project utilizes the service for the purposes of verifying a user's address.

![Email Verification](app/static/images/email_verification_complete.gif)

## Technologies Used

- Flask microframework
- Python for programming
- SendGrid API to handle email needs
- Twilio Verify API for verification
- Flask-bootstrap for responsiveness and aesthetics
- Flask-wtf to create forms
- Python-dotenv to load environment variables

## Features

- Email verification

## Testing

- Clone this repo:
```python
$ git clone git@github.com:GitauHarrison/email-verification-using-twilio-sendgrid-and-flask.git
```

- Change directory to the project's:
```python
$ cd email-verification-using-twilio-sendgrid-and-flask
```

- Create and activate a virtual environment:
```python
$ mkvirtualenv venv # I am using virtualenvwrapper
```

- Install project dependencies:
```python
(venv)$ pip3 install -r requirements.txt
```

- Copy the the contents of `.env-template` to `.env`:
```python
(venv)$ cp .env-template .env
```

- Update `.env` with their values. See how [here](https://github.com/GitauHarrison/notes/blob/master/twilio_sendgrid/04_email_verification.md#working-with-sendgrid).

- Run the application
```python
(venv)$ flask run
```

- Check the application in your favourite browser by pasting the link http://127.0.0.1:5000/. You should be able to see the application.


## Woring with SendGrid

To use SendGrid's API, you need to create an account with them. You can see how to do so [here](https://github.com/GitauHarrison/notes/blob/master/twilio_sendgrid/01_create_acccount.md).

The application has the [`verify_email`](app/verify_email.py) module that uses Twilio Verify service. To create this service, you will need to begin by creating an account with them. It is a short process that you should be able to do quickly. For information, refer to [this](https://github.com/GitauHarrison/notes/blob/master/two_factor_authentication/twilio_verify_2fa.md).

Check how this entire project was made from scratch by refering to this [article](https://github.com/GitauHarrison/notes/blob/master/twilio_sendgrid/04_email_verification.md).
