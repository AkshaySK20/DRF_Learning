import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title":"abc123", "content":"Hello"})
# print(get_response.text)
'''
The above, prints raw text response (almost like a python dictionary.
but, the difference exists between this and JSON like Null and None values for some keys. 
Python dicts will have None instead of Null but, that is reverse for JSON type)
'''
print(get_response.json()) # print as python dictionary
print(get_response.status_code)
