# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACcbb013d8fc080383eabd0108e878c376"
auth_token = "*******"
client = Client(account_sid, auth_token)

def send_message(plant_type, plant_name, days_since):
  message = client.messages.create(body="Remember to water your " + plant_type + ": " + plant_name + "! It has been " + str(days_since) + " days since you last watered " + plant_name + "!",
  from_="+18336926420",
  to="+19192653159")
  print(message.sid)
  return