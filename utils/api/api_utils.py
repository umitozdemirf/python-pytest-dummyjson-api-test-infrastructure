import requests

from config.base_config import BaseConfig


class APIUtils:
    def __int__(self):
        self.api_url = BaseConfig.API_URL

    @staticmethod
    def service_get(path, headers, params=None):
        response = requests.get(BaseConfig.API_URL + path,
                                headers=headers,
                                params=params)
        return response

    @staticmethod
    def service_put(path, headers, body=None):
        response = requests.put(BaseConfig.API_URL + path,
                                data=body,
                                headers=headers)
        return response

    @staticmethod
    def service_post(path, body, headers):
        response = requests.post(BaseConfig.API_URL + path,
                                 data=body,
                                 headers=headers)
        return response

    @staticmethod
    def service_patch(path, body, headers):
        response = requests.patch(BaseConfig.API_URL + path,
                                  data=body,
                                  headers=headers)
        return response

    @staticmethod
    def service_delete(path, headers):
        response = requests.delete(BaseConfig.API_URL + path,
                                   headers=headers)
        return response
