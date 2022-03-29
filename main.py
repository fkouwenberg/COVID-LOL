

from flask import Flask

server = Flask('COVID Dashboard')

@server.route('/')

def index():
  return "A nice COVID dashboard"

@server.route('/summary')

def serve_summary():
  return "Bar chart summary of COVID cases per country"

@server.route('/new')

def serve_summary_new():
  return "Pie chart summary of new COVID cases globally"

@server.route('/netherlands')
def serve_netherlands_history():
  return "Area chart of COVID cases over time in the Netherlands."

server.run('0.0.0.0')

