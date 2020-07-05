# acc sid 
# AC5b422470232f861c9f98ee1a56800df9

# auth token 
# 656171ccec588f8c4c12698528fe3f98

#from twilio.rest import Client

#mynum = "+18560450065"
#twilionum = "+12017787390"

#client = Client("AC5b422470232f861c9f98ee1a56800df9", "656171ccec588f8c4c12698528fe3f98")

#def sendMessage(mainText):
#    client.messages.create(to=mynum,
#                           from_=twilionum, 
#                           body=mainText)

#a = "hey"
#sendMessage(a)

# Download the helper library from https://www.twilio.com/docs/python/install
#from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
#account_sid = 'AC5b422470232f861c9f98ee1a56800df9'
#auth_token = '656171ccec588f8c4c12698528fe3f98'
#client = Client(account_sid, auth_token)

#message = client.messages.create(
#                              body='Hi there!',
#                              from_='+12017787390',
#                              to='+18560450065'
#                          )

#print(message.sid)

import time 
from time import sleep 
from sinchsms import SinchSMS 
  
# function for sending SMS 
def sendSMS(): 
  
    # enter all the details 
    # get app_key and app_secret by registering 
    # a app on sinchSMS 
    number = 'your_mobile_number'
    app_key = 'your_app_key'
    app_secret = 'your_app_secret'
  
    # enter the message to be sent 
    message = 'Hello Message!!!'
  
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' to %s" % (message, number)) 
  
    response = client.send_message(number, message) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    # keep trying unless the status retured is Successful 
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status']) 
  
if __name__ == "__main__": 
    sendSMS() 