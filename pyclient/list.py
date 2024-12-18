import requests
from getpass import getpass #Get password from the console from user


auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username':'admin', 'password':password})

print(auth_response.json()) # print as python dictionary


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/"
    headers = {
        'Authorization': f'Token {token}'
    }
    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json()) # print as python dictionary
    print(get_response.status_code)
