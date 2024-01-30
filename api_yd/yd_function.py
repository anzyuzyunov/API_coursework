import json
import requests
import os
from data.info import headers_dict

def add_folder_yd(name_folder):
    url_new_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    paramss = {
        'path': name_folder
    }

    response = requests.put(url_new_folder,params=paramss, headers=headers_dict)
    print(f'Создана папка с именем {name_folder} на яндекс диске')
    return load_file_in_yd(name_folder)
def load_file_in_yd(name_folder):
    url_YD = 'https://cloud-api.yandex.net'
    up1 = '/v1/disk/resources/upload'
    with open('final_file.json') as fii:
        file = json.loads(fii.read())
    name_photo = []
    for i in file:
        name_photo.append(i['file_name'])
    for i in name_photo:
        paramz = {
            'path': f'{name_folder}/{i}'
        }
        resp = requests.get(f'{url_YD}{up1}',params=paramz,headers=headers_dict)
        href = resp.json()['href']
        with open(f'{i}','rb') as f_up:
            resp = requests.put(href,files={'file':f_up})
            if resp.status_code == 201:
                print(f'Фото {i} загружен на диск')
    print()
    print('Работа программы завершена')



