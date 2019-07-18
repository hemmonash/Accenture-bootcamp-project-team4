from elasticsearch import Elasticsearch
import requests
from flask import Flask, render_template, request
import json
import sendEmail
# from sendEmail import *

client = Elasticsearch()

query_total_defects = {
    "query":{
   "bool":{
     "should": {
         "match": {
           "fields.issuetype.name": "Bug"
         }
       },
       "must" : {
         "bool" :{
           "must_not" : [
             {"match": { "fields.status.statusCategory.name": "Done"}},
             {"match": {"fields.status.statusCategory.name": "Published"}},
             {"match": {"fields.status.statusCategory.name": "Approved"}},
             {"match": {"fields.status.statusCategory.name": "Cancelled"}},
             {"match": {"fields.status.statusCategory.name": "Rejected"}},
             {"match": {"fields.status.statusCategory.name": "Purchased"}},
             {"match": {"fields.status.statusCategory.name": "Accepted"}},
             {"match": {"fields.status.statusCategory.name": "lost"}},
             {"match": {"fields.status.statusCategory.name": "won"}}
             ]
        }
     }
   }
 }
}

res = client.search(index="quality_management_bootcamp", body=query_total_defects)
print("Got %d Hits" % len(res['hits']['hits']))

open_defects = []
for every_hit in res['hits']['hits']:
    result = every_hit['_source']
    open_defects.append(result)

for every in open_defects:
    print(every['fields']['status']['statusCategory']['name'])
print(open_defects)


# read the total number of defects and if the threshhold exceeds the user entered value, send email
total_defects = len(open_defects)

# read the most up-to-date user entered threshold number
user_entered_defects_std_query = client.search(index="alert_index_std")
user_entered_defects_std = int(user_entered_defects_std_query['hits']['hits'][0]['_source']['user_threshold'])
print(user_entered_defects_std)

if (total_defects > user_entered_defects_std):
    # call email function and send email to scrum master
    print("Alter triggered, email will be sent!")
    sendEmail.sendMailToScrumMaster(open_defects)