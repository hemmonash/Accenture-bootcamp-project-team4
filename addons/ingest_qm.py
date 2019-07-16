import json, copy
import requests
from elasticsearch import Elasticsearch

client = Elasticsearch()

url = "https://acnaop.atlassian.net/rest/api/2/search?jql=project='TECHARC' &maxResults=50&total=50"
username = "aiao-tools-team@accenture.com"
password = "xm8SxzxgSm51khUWNKox46B7"
r = requests.get(url, auth=(username,password))

data = json.loads(r.text)

schema = {   "source" : "Jira_defects",
        "fields": {
        "status" : {


            "name": None,
            "statusCategory": {
                "name": None,
                    },
        },
        "priority": {
                        "name": None,
                    },
        "assignee": {
            "name": None,
        },
        "creator": {
            "name": None,
        },
        "reporter": {
            "name": None,
        },
        "issuetype":{
            "name": None,
        },
        "project": {
            "name" : None,
        },
        "created": None,
        "updated": None,
        "resolutiondate": None,
        "aggregatetimeoriginalestimate": None,
        "key": None,
        "timespent": None,
        "summary": None
    }
    }



def checktrue(issue,fields):
    temp = issue[fields[0]]
    for i in range(1,len(fields)):
        try:
            temp = temp[fields[i]]
        except:
            return None
    return temp


i = 0
temp = 0

while True:

    try:
        url = "https://acnaop.atlassian.net/rest/api/2/search?jql=project='TECHARC' &maxResults=50&startAt=" + str(i)
        username = "aiao-tools-team@accenture.com"
        password = "xm8SxzxgSm51khUWNKox46B7"
        r = requests.get(url, auth=(username, password))

        data = json.loads(r.text)
        print(i)

        for index in range(50):
            doc = copy.deepcopy(schema)

            every = data['issues'][index]

            doc['fields']['status']['name'] = checktrue(every, ['fields','status', 'name'])

            doc['fields']['status']['statusCategory']['name'] = checktrue(every,['fields','status','statusCategory','name'])

            doc['fields']['priority']['name'] = checktrue(every,['fields','priority','name'])

            doc['fields']['assignee']['name'] = checktrue(every,['fields','assignee','name'])

            doc['fields']['creator']['name'] = checktrue(every,['fields','creator','name'])

            doc['fields']['reporter']['name'] = checktrue(every,['fields','reporter','name'])

            doc['fields']['issuetype']['name'] = checktrue(every,['fields','issuetype','name'])

            doc['fields']['project']['name'] = checktrue(every,['fields','project','name'])

            doc['fields']['created'] = checktrue(every,['fields','created'])

            doc['fields']['updated'] = checktrue(every,['fields','updated'])

            doc['fields']['resolutiondate'] = checktrue(every,['fields','resolutiondate'])

            doc['fields']['aggregatetimeoriginalestimate'] = checktrue(every,['fields','aggregatetimeoriginalestimate'])

            doc['key'] = checktrue(every,['key'])

            doc['fields']['timespent'] = checktrue(every,['fields','timespent'])

            doc['fields']['summary'] = checktrue(every,['fields','summary'])


            # put to EDB
            Elasticsearch.index(client, "quality_management_index", id = temp, body=doc)
            temp += 1

        i += 50
    except IndexError:
        break


