from twilio.rest import Client

TWILIO_SID = 'AC393ae015001a9ac56f251a24bfa4b437'
TWILIO_AUTH_TOKEN = '272340dbc24be6dd073da81b7aed34ca'
TWILIO_VIRTUAL_NUMBER = "+18125944188"
TWILIO_VERIFIED_NUMBER = "+16262137688"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)