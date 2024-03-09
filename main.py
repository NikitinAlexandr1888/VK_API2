import requests



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

    def return_info(self):
        return {
        "operation_id": "string",
        "href": "string",
        "method": "string",
        "templated": True
        }

    def get_used_space(self):
        return self.get_disk_info().get('bytes_used')
    def download_file(self, path):
        file = open(path, 'rb')
        return file

    def reqest(self, path):
        r = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params={'path': path})
        return r


if __name__ == '__main__':
    vk = VK(TOKEN_VK, ID_VK)
    photos = vk.get_profile_photos()
    print(photos)
