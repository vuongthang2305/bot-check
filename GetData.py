import requests

url = 'http://ddragon.leagueoflegends.com/cdn/11.22.1/data/en_US/champion.json'

res = requests.get(url)
for i in res.json()['data']:
    url_img = f'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{i}_0.jpg'
    res_img = requests.get(url_img)
    with open(f'/home/thang/Desktop/ApiOdoo/champion/{str(i).lower()}.jpg', 'wb') as f:
        f.write(res_img.content)