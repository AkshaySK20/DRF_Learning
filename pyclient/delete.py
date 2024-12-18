import requests

product_id = int(input("What is the product ID you want to delete? \n"))

if product_id:
    print(product_id)
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    #print(get_response.json()) # print as python dictionary
    print(get_response.status_code, get_response.status_code==204)
