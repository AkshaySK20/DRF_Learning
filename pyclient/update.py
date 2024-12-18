import requests

endpoint = "http://localhost:8000/api/products/13/update/"

data = {
    'title':'Yooooo, This is an update!',
    'price':10.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json()) # print as python dictionary
print(get_response.status_code)
