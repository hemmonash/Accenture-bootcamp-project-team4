from elasticsearch import Elasticsearch
import requests
from flask import Flask, render_template, request
from sendEmail import *

client = Elasticsearch()

# read the total number of defects and if the threshhold exceeds the user entered value, send email
total_defects = client.search(index="total_defect_index")

# read the most up-to-date user entered threshold number
user_entered_defects = client.search(index="alert_index")

# run query to get the open defects 


if (total_defects > user_entered_defects):
    # call email function and send email to scrum master
    sendMailToScrumMaster()
