

from requests import get
import logging

URL_API = "http://api.covid19api.com"

def download_summary():
  response = get(f"{URL_API}/summary")
  if response.status_code == 200:
    return response.json()
  else: #show error message
    logging.error(f'An error has occurred: HTTP status {response.status_code}')
    return{}

def download_confirmed_per_country(country):
  response = get(f'{URL_API}/country/{country}/status/confirmed')
  if response.status_code == 200:
    logging.info('Serve Dutch Data')
    return {"data" : response.json()}
  else:#show error message
    logging.error(f'An error has occurred: HTTP status {response.status_code}')
    return{}





