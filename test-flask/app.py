from elasticsearch import Elasticsearch
import requests
from flask import Flask, render_template, request

client = Elasticsearch()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return render_template('form_template.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      # the result contains the threshold number
      doc = {
         'user_threshold': int(result['threshold'])
      }
      try:
         Elasticsearch.index(client, "alert_index", id='1', body=doc) 
         # once successful listen for defect numbers
         # cron schedule: 0 * * * *  /home/bootcamp/addons/<script name> 
      except:
         print('ERROR')
      return render_template("result_template.html",result = result)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)