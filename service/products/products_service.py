import json

from config.service.service_config import ServiceConfig

from utils.api.api_utils import APIUtils as api_utils
from utils.assertion.assertion import Assertion as assertion

from model.product import PRODUCT


class ProductService:

    @staticmethod
    def get_products():
        path = ServiceConfig.PRODUCTS
        headers = {'Content-Type': "application/json"}
        params = {'limit': 100}

        response = api_utils.service_get(path,
                                         headers,
                                         params)
        assert response.status_code == 200, "Status code is not 200!"
        assertion.is_not_null("response", response.json())

        return response.json()

    @staticmethod
    def create_product():
        path = ServiceConfig.PRODUCTS + ServiceConfig.ADD
        headers = {'Content-Type': "application/json"}

        response = api_utils.service_post(path, json.dumps(PRODUCT), headers)

        assert response.status_code == 200, "Status code is not 200!"  # should be 201!
        assertion.is_not_null("response", response.json())

        return response.json()

    @staticmethod
    def delete_product(product_id):
        path = f"{ServiceConfig.PRODUCTS}/{product_id}"
        headers = {'Content-Type': "application/json"}

        response = api_utils.service_delete(path, headers)

        assert response.status_code == 404, "Status code is not 404!"
        assertion.is_not_null("response", response.json())

        return response.json()
