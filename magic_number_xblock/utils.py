import requests
from requests.auth import HTTPBasicAuth
from .config import AUTH_URL, CLIENT_ID, CLIENT_SECRET, MAGIC_NUMBER_URL


def get_headers():
    response = requests.post(AUTH_URL,
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                             data={"grant_type": "client_credentials"})
    data = response.json()
    access_token = data['access_token']
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    return headers


def get_magic_number():
    response = requests.get(MAGIC_NUMBER_URL)
    res_data = response.json()
    number = res_data['number']
    return number


def create_or_update_magic_number(number):
    headers = get_headers()
    data = {'number': number}
    db_number = get_magic_number()
    if db_number:
        response = requests.put(MAGIC_NUMBER_URL, headers=headers, data=data)
    else:
        response = requests.post(MAGIC_NUMBER_URL, headers=headers, data=data)
    res_data = response.json()
    number = res_data['number']
    return number
