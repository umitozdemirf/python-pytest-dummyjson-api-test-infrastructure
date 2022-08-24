import json

import requests

from config.service.service_config import ServiceConfig

from utils.api.api_utils import APIUtils as api_utils
from utils.assertion.assertion import Assertion as assertion


class CartsService:

    @staticmethod
    def get_carts():
        path = ServiceConfig.CARTS
        headers = {'Content-Type': "application/json"}

        response = api_utils.service_get(path,
                                         headers)

        assert response.status_code == 200, "Status code is not 200!"
        assertion.is_not_null("response", response.json())

        return response.json()['carts']
