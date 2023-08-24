from twilio.rest import Client
import smtplib, ssl

def send(sendername,sendermail,sendermessage):
    account_sid = 'ACcef77bcf01e1cbc29d1610e9eaf8186a'
    auth_token = '8579aefc6e45d60281e3ba7f8351e61b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body="You have a new message from,"+ sendername +" : " +sendermail+" : " + sendermessage,
    to='whatsapp:+919403578011'
    )

    print(message.sid)


def sendMail(sendername,sendermail,sendermessage):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"  
    receiver_email = "your@gmail.com" 
    password = ""
    message = """
    Subject: Hi there you have a message from 

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    

