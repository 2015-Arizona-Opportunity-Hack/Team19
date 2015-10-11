__author__ = 'saipc'

import smtplib
from email.mime.text import MIMEText

def generateEmail(name, message, image):
    email = """
<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title></title></head><body>
<div class="body" width="600" style="color: #000088; font-size: 20px"><table cellpadding="5"><tbody style="padding: 12px;">
<tr><th colspan="4"><img src="header.jpg" width="600"></th></tr>
<tr><td colspan="2" style="padding: 12px;"><p>Dear Mr. """ + name + """</p>
<p>""" + message + """</p></td><td colspan='1'><img src='""" + image + """'></td></tr>
<tr><td colspan="4"><img src="footer.jpg" width="600"></td></tr></tbody></table></div></body></html>
"""
    return email

def sendEmail(email, address):

    msg = MIMEText(email, 'html')
    me = "schand31@asu.edu"
    # me == the sender's email address
    msg['Subject'] = 'Thank You note from SupportMyClub'
    msg['From'] = me
    msg['To'] = address

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
    server.login("schand31", "1123581321Fs+")
    server.sendmail(me, [address], msg.as_string())
    server.quit()

if __name__ == "__main__":
    email = generateEmail("Swetha", "Poya yov", "http://i.forbesimg.com/media/lists/companies/google_416x416.jpg")
    them = "swetha.baskaran@asu.edu"
    sendEmail(email, them)
