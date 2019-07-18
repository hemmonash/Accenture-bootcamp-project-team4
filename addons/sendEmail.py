from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def sendMailToScrumMaster(defect_obj):
    """
    defect_objs: param for the defect objects
    """
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    password = "bootcamp1234"
    msg['From'] = "accenturebootcampteam4@gmail.com"
    msg['To'] = "kdas0001@student.monash.edu" #"asfiya.memon@accenture.com" #["febinaly@getnada.com", "aditivenkateshr@gmail.com", "asfiya.memon@accenture.com", "krishnendu.c.das@accenture.com", "chethzz@hotmail.com", "peter.liang.official@gmail.com", "riababyc@gmail.com"]
    msg['Subject'] = "Defect threshold exceeded!"

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # s.login(msg['From'], password)

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    # create message object instance
    # msg = MIMEMultipart('alternative')
    # message = '<p>HELLOW WORLD</p><a href="#">asdsadsa</a>'
    # message = '''
    # <!DOCTYPE html>
    # <html lang="en">

    # <head>
        
    #     <meta charset="utf-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1">
    #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    #     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">

    #     <style>
    #         /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    #         .row.content {
    #             height: 550px
    #         }

    #         /* Set gray background color and 100% height */
    #         .sidenav {
    #             background-color: #f1f1f1;
    #             height: 100%;
    #         }

    #         /* On small screens, set height to 'auto' for the grid */
    #         @media screen and (max-width: 767px) {
    #             .row.content {
    #                 height: auto;
    #             }
    #         }
    #     </style>
    # </head>

    # <body>
    #     <center>
    #     <table class="table">
    #     <thead>
    #         <tr>
    #         <th scope="col">Defect #</th>
    #         <th scope="col">Defect ID</th>
    #         <th scope="col">Project Name</th>
    #         <th scope="col">Assignee Name</th>
    #         <th scope="col">Last Updated</th>
    #         <th scope="col">Project Summary</th>
    #         </tr>
    #     </thead>
    #     <tbody>
    # '''
    # print(defect_obj)
    # row_index = 1
    # for every_defect in defect_obj:
    #     # assigne name, last up
    #     defect_id = every_defect['fields']['project']['key']
    #     assignee_name = every_defect['fields']['assignee']['name']
    #     last_updated = every_defect['fields']['updated']
    #     project_name = every_defect['fields']['project']['name']
    #     project_summary = every_defect['fields']['summary']

    #     table_row_entry = '<tr><th scope="row">{}</th><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(row_index, defect_id, project_name, assignee_name, last_updated, project_summary)
    #     print(table_row_entry)
    #     message += table_row_entry
    #     row_index += 1

    # message += '''
    #     </tbody>
    #     </table>
        
    #     </center>
    # </body>
    # </html>
    # '''
    # setup the parameters of the message
    # password = "bootcamp1234"
    # msg['From'] = "accenturebootcampteam4@gmail.com"
    # msg['To'] = "kdas0001@student.monash.edu" #"asfiya.memon@accenture.com" #["febinaly@getnada.com", "aditivenkateshr@gmail.com", "asfiya.memon@accenture.com", "krishnendu.c.das@accenture.com", "chethzz@hotmail.com", "peter.liang.official@gmail.com", "riababyc@gmail.com"]
    # msg['Subject'] = "Defect threshold exceeded!"

    # # add in the message body
    # msg.attach(MIMEText(message, 'plain'))

    # # create server
    # server = smtplib.SMTP('smtp.gmail.com: 587')

    # server.starttls()

    # # Login Credentials for sending the mail
    # server.login(msg['From'], password)

    # # send the message via the server.
    # server.sendmail(msg['From'], msg['To'], msg.as_string())

    # server.quit()

    # print("successfully sent email to %s:" % (msg['To']))