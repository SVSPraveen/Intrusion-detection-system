from twilio.rest import Client

def sendSms():
  account_sid = 'AC610c15e0166d13ef158ba10f3ef271f5'
  auth_token = '[AuthToken]'
  client = Client(account_sid, auth_token)
  message = client.messages.create(
  from_='+16056006819',
  body='Alert',
  to='+18777804236'
)
  print("Message sent:", message.sid)
 