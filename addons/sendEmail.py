from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def sendMailToScrumMaster(defect_obj):
    """
    defect_objs: param for the defect objects
    """
    # create message object instance
    msg = MIMEMultipart()
    message = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <title>Alert config page</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">

        <style>
            /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
            .row.content {
                height: 550px
            }

            /* Set gray background color and 100% height */
            .sidenav {
                background-color: #f1f1f1;
                height: 100%;
            }

            /* On small screens, set height to 'auto' for the grid */
            @media screen and (max-width: 767px) {
                .row.content {
                    height: auto;
                }
            }
        </style>
    </head>

    <body>
        <center>
        <table class="table">
        <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
            </tr>
        </thead>
        <tbody>
    '''
    print(defect_obj)
    row_index = 1
    for every_defect in defect_obj:
        # assigne name, last up
        defect_id = int(every_defect['key'])
        assignee_name = every_defect['fields']['assignee']['name']
        last_updated = every_defect['fields']['updated']
        project_name = every_defect['fields']['project']['name']
        project_summary = every_defect['fields']['summary']

        message += ('<tr><th scope="row">%d</th><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>', row_index, defect_id, project_name, assignee_name, last_updated, project_summary)
        row_index += 1

    message += '''
        </tbody>
        </table>
        </center>
    </body>
    </html>
    '''
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