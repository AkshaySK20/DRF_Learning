import requests

endpoint = "http://localhost:8000/api/products/16/"

get_response = requests.get(endpoint)

print(get_response.json()) # print as python dictionary
print(get_response.status_code)
