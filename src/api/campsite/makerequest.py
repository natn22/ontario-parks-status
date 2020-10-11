import requests
from requests.exceptions import HTTPError

ONTARIO_PARKS_API_URL = "https://reservations.ontarioparks.com/api"

# GET
def get_request(route):
  url = ONTARIO_PARKS_API_URL + route
  try:
    response = requests.get(url)
    response.raise_for_status()
  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')
  else:
    return response.json()


# POST
def post_request(route, data):
  url = ONTARIO_PARKS_API_URL + route
  try:
    headers = {'Content-type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')
  else:
    return response.json()