import smtplib
import urllib.request as urllib2
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib2.urlopen("http://216.58.192.142", timeout=1)
        return True
    except urllib2.URLError as error:
        print("Connection Error:", error)
        return False


def mail_sender(filename, generated_time):
    from_address = "tjagtap258@gmail.com"
    to_address = "tjagtap25800@gmail.com"
    gmail_password = "tdj@28091997"

    msg = MIMEMultipart()
    msg['from'] = from_address
    msg['to'] = to_address
    body = """
    Hello,
    Please Find Attached document which contains Log of all process running.
    Log is created at: %s

    This is auto generated mail.

    Thanks & Regards
    Tushar Jagtap   
    """ % generated_time
    subject = """
    Process log generated at : %s""" % generated_time
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename = %s " % filename)
    msg.attach(p)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(from_address, gmail_password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Log File Successfully Send through mail")
    except Exception as e:
        print("unable to send email", e)



