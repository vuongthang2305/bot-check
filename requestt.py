from os import times
from PIL.ImageFilter import Color3DLUT
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, time
import os
from bs4 import BeautifulSoup
def cralw(name):
    data = {}
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=720x480")
        path = os.path.dirname(__file__) + "/chromedriver"
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
        driver.get(f"https://lmssplus.com/profile/{name}")
        rank = driver.find_element_by_class_name("rankBox_rankName__VcGiL")

        if len(rank.text) == 1:
            data = {
                'code': 404,
                'message': f'Không tìm thấy tài khoản `{name}` vui lòng kiểm tra lại',
            }
            driver.quit()
        else:
            summoner_name = driver.find_element_by_class_name("nameAndImg_name__b_gpp")
            level = driver.find_element_by_class_name("nameAndImg_level__327IV")
            champ = driver.find_elements_by_class_name("masteries_tqOneName__1JV7r")
            score_champ = driver.find_elements_by_class_name("masteries_tqOneSortDetail__2VgWs")
            history_status = driver.find_elements_by_class_name("historyBox_metaInfosStatus__Wi3Pq")
            time.sleep(1)
            

            print(len(history_status))
            status = [i.text for i in history_status]

            print(rank.text)
            data = {
                'code': 200,
                "summoner_name": summoner_name.text,
                "level": level.text,
                "rank": rank.text,
                "champ_top": {
                    "champ_name": str(champ[1].text).capitalize(),
                    "score": str(score_champ[2].text).split(' ')[0]
                },
                "champ_mid": {
                    "champ_name": str(champ[0].text).capitalize(),
                    "score":str(score_champ[0].text).split(' ')[0]
                },
                "champ_jungle": {
                    "champ_name": str(champ[2].text).capitalize(),
                    "score": str(score_champ[4].text).split(' ')[0]
                },
                "history": status,
            }
            time.sleep(1)
            driver.quit()
    except Exception as e:
        print(e)
        data = {
            'code': 500,
            'message': 'Lỗi hệ thống',
        }
    return data