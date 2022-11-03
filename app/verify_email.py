from app import app
from twilio.rest import Client, TwilioException


def _get_twilio_verify_client():
    """
    Get the Twilio Verify API client
    """
    return Client(
        app.config['TWILIO_ACCOUNT_SID'],
        app.config['TWILIO_AUTH_TOKEN']
    ).verify.services(app.config['TWILIO_VERIFY_SERVICE_ID'])


def request_email_verification_token(email):
    """Generate a token to be sent to client email"""
    verify = _get_twilio_verify_client()
    verify.verifications.create(to=email, channel='email')


def check_email_verification_token(email, token):
    """Client's token is verified"""
    verify = _get_twilio_verify_client()
    try:
        result = verify.verification_checks.create(to=email, code=token)
        return result.status == 'approved'
    except TwilioException as e:
        return False
