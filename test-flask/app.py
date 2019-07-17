from elasticsearch import Elasticsearch
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return render_template('form_template.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   client = Elasticsearch()
   if request.method == 'POST':
      result = request.form
      # the result contains the threshold number
      alert_index_std = {
         'user_threshold': int(result['threshold_std']),
      }

      alert_index_dyn = {
         'user_threshold': int(result['threshold_dyn']),
      }

      scrum_master_email_std = {
         'email': result['email_std']
      }

      scrum_master_email_dyn = {
         'email': result['email_dyn']
      }

      print(alert_index_std, alert_index_dyn, scrum_master_email_std, scrum_master_email_dyn)
      
      try:
         # save the threshold values
         Elasticsearch.index(client, "alert_index_std", id='1', body=alert_index_std) 
         Elasticsearch.index(client, "alert_index_dyn", id='1', body=alert_index_dyn) 

         # save the scrum master email values
         Elasticsearch.index(client, "scrum_master_email_std", id='1', body=scrum_master_email_std) 
         Elasticsearch.index(client, "scrum_master_email_dyn", id='1', body=scrum_master_email_dyn) 

         print('SUCCESS!')
         # once successful listen for defect numbers
         # cron schedule: 0 * * * *  /home/bootcamp/addons/<script name> 
         return render_template("result_template.html",result = result)
      except:
         print('ERROR')
         return render_template("fail_template.html",result = result)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)