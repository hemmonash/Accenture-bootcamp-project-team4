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
        <div class="jumbotron" style="margin: 5%;">
        <h1 class="display-3">Defect threshold has been passed!</h1>
        <p class="lead">The defect threshold has been crossed and below are the details</p>
        <hr class="my-4">
        <p>You can always re-configure alert details <a href="https://techbootcamp.mywizard360.com/melbootcamp2019julyt4_5000">here</a></p>
        <p class="lead">
        
        <table class="table">
        <thead>
            <tr>
            <th scope="col">Defect #</th>
            <th scope="col">Defect ID</th>
            <th scope="col">Project Name</th>
            <th scope="col">Assignee Name</th>
            <th scope="col">Last Updated</th>
            <th scope="col">Project Summary</th>
            </tr>
        </thead>
        <tbody>
    '''
    print(defect_obj)
    row_index = 1
    for every_defect in defect_obj:
        # assigne name, last up
        defect_id = every_defect['fields']['project']['key']
        assignee_name = every_defect['fields']['assignee']['name']
        last_updated = every_defect['fields']['updated']
        project_name = every_defect['fields']['project']['name']
        project_summary = every_defect['fields']['summary']

        table_row_entry = '<tr><th scope="row">{}</th><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(row_index, defect_id, project_name, assignee_name, last_updated, project_summary)
        print(table_row_entry)
        message += table_row_entry
        row_index += 1

    message += '''
        </tbody>
        </table>
        <a class="btn btn-primary btn-lg" href="https://techbootcamp.mywizard360.com/melbootcamp2019julyt4_5601/app/kibana#/dashboard/9c7ca7e0-a861-11e9-8eee-e33d10f51134?_g=(filters%3A!()%2CrefreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3A'2016-09-28T15%3A05%3A52.732Z'%2Cto%3A'2019-07-31T14%3A00%3A00.000Z'))" role="button">Go to Dashboard!</a>
        </p>
        </div>
        </center>
    </body>
    </html>
    '''
    # setup the parameters of the message
    password = "bootcamp1234"
    msg['From'] = "accenturebootcampteam4@gmail.com"
    msg['To'] = "aditivenkateshr@gmail.com" #"asfiya.memon@accenture.com" #["febinaly@getnada.com", "aditivenkateshr@gmail.com", "asfiya.memon@accenture.com", "krishnendu.c.das@accenture.com", "chethzz@hotmail.com", "peter.liang.official@gmail.com", "riababyc@gmail.com"]
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