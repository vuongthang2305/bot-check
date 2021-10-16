import json
from mmap import ACCESS_COPY
from typing import cast
import requests
import sys
from python.lazop.base import LazopClient, LazopRequest,sign
from datetime import datetime
import hmac
import hashlib

APP_KEY = 102554
APP_SECRET = 'WiwfDkCjn6VyA2RGUXlcaPrsHPISOqyM'
URL = 'https://api.lazada.vn/rest'
ACCESS_TOKEN = '50000501f40fYKcq5muvFFeLIVGQUDE5DwxAQrxxsu01gtCJaPdu185bfe1cgj1'

# return timestamp
def get_timestamp():
    now = datetime.now()

    timestamp = int(datetime.timestamp(now)) * 1000
    return timestamp

params = {
        
        "app_key": APP_KEY,
        "sign_method": 'sha256',
        "timestamp": get_timestamp(),
    }

# get category 
def get_category():
    # '/category/tree/get'
    api = '/category/tree/get'
    url = URL + api

    params['language_code'] = 'vi_VN'
    params['access_token'] = ACCESS_TOKEN
    sign_code = sign(APP_SECRET,api, params)
    params['sign'] = sign_code
    
    res = requests.request('GET', url=url, params=params)
    
    return res
    # with open('data1.json', 'w', encoding='utf-8') as f:
    #     json.dump(res.json(), f, ensure_ascii=False, indent=4)


def read_json(filename):
    f = open(filename, 'r', encoding='utf-8')
    data = json.load(f)
    file = open('data3.txt','a', )
    
    
    for res in data['data']:
        file.write(res['name']+'\n')
        for item in res['children']:
            if item['name'] not in res['children']:
                pass
            print (item['name'])

        
    file.close()

# get code 
def authorization(url_callback):
    auth_url = f'https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri={url_callback}&client_id={APP_KEY}'
    return auth_url  


def get_acceccs_token(code):
    url = URL + '/auth/token/create'
    params = {
        
        "app_key": APP_KEY,
        "sign_method": 'sha256',
        "timestamp": 1634264114380,
    }
    params['code'] = code
    params['sign'] = sign(APP_SECRET,'/auth/token/create' ,params)
    
    print (sign(APP_SECRET,'/auth/token/create' ,params))
    res = requests.request('GET', url, params=params)

    return res.json()

# Error Invalid authorization code wait support
# Override method access_token
def get_acceccs_token(code):
    client = LazopClient(URL, APP_KEY ,APP_SECRET)
    request = LazopRequest('/auth/token/create')
    request.add_api_param('code', '0_102554_o7YcxyR9fXUFO3ChHqIKmb27238')

    response = client.execute(request)
    print(response.type)
    print(response.body)


def get_all_products():
    url = URL + '/products/get'
    params = {
        "app_key": APP_KEY,
        "sign_method": 'sha256',
        "timestamp": 1634267225109,
    }
    params['filter'] = 'live'
    params['access_token'] = '50000501f40fYKcq5muvFFeLIVGQUDE5DwxAQrxxsu01gtCJaPdu185bfe1cgj1'
    params['sign'] = sign(APP_SECRET,'/products/get' ,params)

    res = requests.get(url, params=params)
    return res

# print(authorization('https://buiquocviet171020.wixsite.com/my-site-1'))


f = open('data1.json', 'r', encoding='utf-8')
js = json.load(f)
for i in js['data']:

    for item in i['children']:
        print ('\t',item['category_id'], item['name'])

       
        
            
                