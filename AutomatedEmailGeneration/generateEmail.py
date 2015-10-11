#!/usr/bin/python2.7

print "Content-type: text/html"
print "\r\n"

__author__ = 'saipc'

import smtplib
from email.mime.text import MIMEText

def generateEmail(name, message, image):
    email = """
<!DOCTYPE html><html><head lang=en><meta charset='UTF-8'><meta property='og:url' content='https://apps.facebook.com/supportmyclubapp/'>
</head><body>""" + """
<div class="body" width="600" style="color: #000088; font-size: 20px">
<a style='display:block;' href='http://www.supportmyclub.org/'>
<table cellpadding="5"><tbody style="padding: 12px;">
<tr><th colspan="5"><img src="http://s17.postimg.org/g2z6jnlnz/header.jpg" width="600"></th></tr>
<tr><td colspan="3" style="padding: 12px;"><p>Dear """ + name + """,</p>
<p>""" + message + """</p></td><td colspan='2'><img src='""" + image + """' width='200'></td></tr>
<tr><td colspan="5"><img src="http://s17.postimg.org/y7274ajcf/footer.jpg" width="600"></td></tr>
</td></tr></tbody></table></a>
<p><a href='https://www.facebook.com/sharer/sharer.php?u=https://apps.facebook.com/supportmyclubapp/'><img src='http://bitcoin-catcher.com/wp-content/uploads/2015/09/facebook-share-button.png' width='100' alt='Share on Facebook'></a></p>
</div></body></html>
"""
    return email

def sendEmail(email, address, subject):

    msg = MIMEText(email, 'html')
    me = "saipc1993@gmail.com"
    # me == the sender's email address
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = address

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #socket = server._get_socket()
    #Next, log in to the server
    server.login("saipc1993", "dragondragon")
    server.sendmail(me, [address], msg.as_string())
    server.quit()

if __name__ == "__main__":
    email = generateEmail("Dilip", "Hey thank you so much for giving <br>us this great opportunity", "http://i.forbesimg.com/media/lists/companies/google_416x416.jpg")
    them = "sndilip17@gmail.com"
    print "Thank You Email successfully sent to ", them
    print email
    sendEmail(email, them, 'Thank You note from SupportMyClub')
