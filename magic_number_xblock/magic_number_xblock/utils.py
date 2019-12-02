import requests
from requests.auth import HTTPBasicAuth

AUTH_URL = "http://localhost:8000/o/token/"
MAGIC_NUMBER_URL = "http://localhost:8000/number/"
CLIENT_ID = "lxQnZzvhD9o6Y6rBCij2J0ozVAVqcnWlSsRoYISg"
CLIENT_SECRET = "2y8ggWb6DHv3OY9lAQJUef3HZazzbLwMiJXjEdt8mX1IZaTKVcS4vMnzXnPe1CwwphacNfMBPyhoXwyVxvsKoRjhVXhvltN4RIxZmveXsvZe464IVScF4Gm1qSJXioBM"  # noqa


def get_headers():
    response = requests.post(AUTH_URL,
                             auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                             data={"grant_type": "client_credentials"})
    data = response.json()
    access_token = data['access_token']
    headers = {'Authorization': 'Bearer %s'.format(access_token)}
    return headers


def get_magic_number():
    response = requests.get(MAGIC_NUMBER_URL)
    res_data = response.json()
    number = res_data['number']
    return number


def create_or_update_magic_number(number):
    headers = get_headers()
    data = {'number': number}
    if isinstance(number, int):
        response = requests.put(MAGIC_NUMBER_URL, headers=headers, data=data)
    else:
        response = requests.post(MAGIC_NUMBER_URL, headers=headers, data=data)
    res_data = response.json()
    number = res_data['number']
    return number
