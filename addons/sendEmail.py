from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendMailToScrumMaster(defect_objs):
    """
    defect_objs: param for the defect objects
    """
    # create message object instance
    msg = MIMEMultipart()

    message = ""

    # setup the parameters of the message
    password = "bootcamp1234"
    msg['From'] = "accenturebootcampteam4@gmail.com"
    msg['To'] = "febinaly@getnada.com"
    msg['Subject'] = "Defect threshold exceeded!"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))