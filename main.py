

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for filename in file_list:
            href = self._get_upload_link(file_path=filename).get("href", "")
            response = requests.put(href, data=open(filename, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


file_list = ['text_1', 'text_2', 'text_for_yandex']


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r"C:\Users\shiri\PycharmProjects\requests_task_2\text_1"
    token = "AQAAAAAdY_7xAADLW9xEtgeYuEedowT0BNUTzfs"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
