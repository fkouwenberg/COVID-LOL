

from covid import download_summary, download_confirmed_per_country
from flask import Flask

import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)

import json

server = Flask('COVID Dashboard')

@server.route('/')

def index():
  return server.send_static_file('index.html')

@server.route('/summary')

def serve_summary():
  json_template = json.load(open("templates/summary.json"))
  json_data = download_summary()
  json_template["data"]["values"] = json_data["Countries"]
  return json_template

@server.route('/new')

def serve_summary_new():
  json_template = json.load(open("templates/new.json"))
  json_data = download_summary()
  values = []
  
  for key in json_data["Global"]:
    if key.startswith("New"):
      value = {"category": key, "value": json_data["Global"][key]}
      values.append(value)
  json_template["data"]["values"] = values
  return json_template

@server.route('/netherlands')

def serve_netherlands_history():
  json_template = json.load(open("templates/history.json"))
  json_data = download_confirmed_per_country("netherlands")
  json_template["data"]["values"] = json_data["data"]
  return json_template

server.run('0.0.0.0')

