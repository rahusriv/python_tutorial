"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib, ssl

context = ssl.create_default_context()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) #587)



#Next, log in to the server
server.login("rahusr", "M@stL@ppy123l")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "rahusr@gmail.com", msg)