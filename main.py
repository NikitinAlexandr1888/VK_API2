from urllib.parse import urlencode
from time import sleep
import requests
import json
import vk_api
import posixpath
import os
import yadisk


ID_VK = input("ID_VK: ")
TOKEN_VK = input('TOKEN_VK: ')

class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_profile_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

class YADISK:
    def __init__(self, token, path):
        self.token = token
        self.path = path

    def get_disk_info(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(url, headers=headers)
        return response.json()

    def mkdir(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code

    def upload(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path}
        response = requests.get(url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    vk = VK(TOKEN_VK, ID_VK)
    photos = vk.get_profile_photos()
    print(photos)

#     y = yadisk.YaDisk(token="токен")
#
#     # Создаёт новую папку "/test-dir"
#     print(y.mkdir("/test-dir"))
#     to_dir = "/test-dir"
#     from_dir = "to_upload"
#
#     # проверка свободного места
#     fields = y.get_disk_info().FIELDS
#     free_space = (fields['total_space'] - fields['used_space']) / 1048576
#     trash = fields['trash_size'] / 1048576
#     print(f"свободное место на yandex disk: {round(free_space, 2)} Мб", )
#     print(f"корзина занимает: {round(trash, 2)} Мб", )
#
#
#     def recursive_upload(y, from_dir, to_dir):
#         for root, dirs, files in os.walk(from_dir):
#             p = root.split(from_dir)[1].strip(os.path.sep)
#             dir_path = posixpath.join(to_dir, p)
#
#             for file in files:
#                 file_path = posixpath.join(dir_path, file)
#                 in_path = os.path.join(from_dir, file)
#                 print(in_path)
#                 try:
#                     y.upload(in_path, file_path)
#                 except yadisk.exceptions.PathExistsError as e:
#                     print(e)
#
#
#     recursive_upload(y, from_dir, to_dir)
#     print("залито")
#
#     for f in list(y.listdir(to_dir)):
#         y.publish(f'{to_dir}/{f.FIELDS["file"].split("&")[1].split("=")[1]}')  # make file public
#
#     with open("links.txt", "a") as l:
#         for f in list(y.listdir("/test-dir")):
#             print(f.FIELDS["public_url"])  # public url
#             l.write(f.FIELDS["public_url"] + '\n')
#
#     print('готово')
#
# if __name__ == '__main__':
#     vk = VK(TOKEN_VK, ID_VK)
#     print(vk.users_info())
#     print(vk.get_profile_photos())