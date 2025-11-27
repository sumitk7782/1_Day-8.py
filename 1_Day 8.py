from twilio.rest import Client
ACCOUNT_STD="YOUR ACCOUNT_SID "
AUTH_TOKEN="YOUR AUTH_NUMBER"
TWILIO_NUMBER="TWILIO_NUMBER"
RECIVER_NUMBER="YOUR RECIVER NUMBER"
client = Client(ACCOUNT_STD, AUTH_TOKEN)

message = client.messages.create(
    body="Hello, I am Media and I sent this message from Python!",
    from_=TWILIO_NUMBER,
    to=RECIVER_NUMBER
)
print("Message sent! message STD:",message.STD)