import json

import requests
from pprint import pprint
from urllib.parse import urlencode
def add_access_token():
    url_vk = 'https://oauth.vk.com/authorize'
    idvk_test = '51838929'
    param = {
        'client_id': idvk_test,
        'display': 'page',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'scope': 'photos',
        'response_type': 'token',
        'v': '5.199'
    }


    oauth_url = f'{url_vk}?{urlencode(param)}'
    print(oauth_url)
access_token = 'Тут токен от ВК'


url_request = 'https://api.vk.com/method/'

def info():
    id = input('Введите ID VK ')
    count = input('Введите количество загружаемых фото, по умолчанию будет загружено 5 ')
    if not count:
        count = 5
        return get_photo(user_id=id,count_photo=count)
    else:
        return get_photo(user_id=id,count_photo=count)
def get_photo(user_id,count_photo):
    metod_get_photo = 'photos.get?'
    params_get_photo = {
        'access_token': access_token,
        'v': '5.199',
        'user_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'count': count_photo,
        'photo_sizes': 1
    }

    resp = requests.get(f'{url_request}{metod_get_photo}',params=params_get_photo)
    dump = resp.json()
    with open('vk_photos.json','w') as f:
        json.dump(dump,f,indent=4,ensure_ascii=False)



def file_processing():
    with open('vk_photos.json') as f:
        file = json.load(f)
    tt = []
    for i in file['response']['items']:
        id_photo = i['id']
        size = ''
        image = i['sizes'][-1]['url']
        like = i['likes']['count']

        for id in i['sizes']:
            if id['url'] == image:
                size += (id['type'])
        tt.append({'file_name': f'{like}_{id_photo}.jpg',
                   'size': size})
        response = requests.get(image)
        with open(f'{like}_{id_photo}.jpg', 'wb') as file:
            file.write(response.content)
    with open('final_file.json','w') as file_all:
        json.dump(tt,file_all,indent=4,ensure_ascii=False)
        print(f'Сформирован фаил с данным final_file.json')


