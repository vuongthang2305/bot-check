import json
import os
import xmlrpc.client
from PIL import Image
import base64
from io import BytesIO
from time import sleep
from datetime import datetime

url = 'http://odoo14.xyz'
db = 'odoo14'
# 480f54add5eb89ef09eb873ed757d0ba26f1602b
username = 'admin'
password = 'admin'



common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
uid = common.authenticate(db, username, password,{})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


def save_product():
    ids_product = models.execute_kw(db, uid, password, 'product.template', 'search', [[]])
    print(ids_product)

    for id in ids_product:
        record = models.execute_kw(db, uid, password,'product.template', 'read',[id])

        for i in record:
            for j in i:
                if 'image_' in str(j):
                    save_file(str(i[j]), i['name'])
                    continue
data = ''
def save_file(data, filename):
    imgdata = base64.b64decode(data)
    filename = f'{filename}.jpg'  
    with open(filename, 'wb') as f:
        f.write(imgdata)


def get_time_utc():
    
    return datetime.utcnow()

print (str(get_time_utc()).split('.')[0])