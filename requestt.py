import requests
import json


def get_Token():
    url = 'https://open.sendo.vn/login'

    headerss = {
        'Content-Type': 'application/json'
    }

    data = {
        "shop_key":"6e8591b5b33e42209bcd6ae8b6ca1595",
        "secret_key":"fce83a72d24844c1be4a71ae1e459ae4"
    }
    data = json.dumps(data)
    response = requests.request("POST", url, headers=headerss, data=data)
    return response.json()['result']['token']

TOKEN = get_Token()

def get_category():
    url = 'https://open.sendo.vn/api/partner/category/0'
    

    headers ={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
    }

    response = requests.request("GET", url, headers=headers)

    return response

def get_product():
    url = 'https://open.sendo.vn/api/partner/product/search'

    TOKEN = get_Token()

    headers = {
        'authorization': 'bearer ' + TOKEN, 
        'Content-Type': 'application/json',
        'cache-control': 'no-cache'
    }

    data = {
    "page_size": 10,
    "product_name": "",
    "date_from": "2020-05-01",
    "date_to": "2021-10-28",
    "status":'',
    "token": ""
	}
    data = json.dumps(data)
    
    response = requests.request("POST", url, headers=headers, data=data)
    return response.json()


def get_detail_product(id):
    url = f'https://open.sendo.vn/api/partner/product?id={id}'

    headers = {
        'Authorization': 'bearer {}'.format(TOKEN) 
    }
    
    response = requests.request("GET", url, headers=headers)

    return response.json()

id = ''
for i in get_product()['result']['data']:
    id = i['id']
data = get_detail_product(id)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)