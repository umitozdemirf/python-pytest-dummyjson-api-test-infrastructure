import logging

import pytest

from utils.data.data_generator import DataGenerator as generator
from utils.assertion.assertion import Assertion as assertion
from service.products.products_service import ProductService as product_service
from model.product import PRODUCT, PRODUCT_RESPONSE_BODY


class TestProducts:
    """Products tests - """

    @pytest.mark.smoke
    def test_get_products(self):
        resp = product_service.get_products()

        for k, v in PRODUCT_RESPONSE_BODY.items():
            assertion.is_not_null(k, resp[k])

    @pytest.mark.smoke
    def test_create_product(self):
        resp = product_service.create_product()

        for k, v in PRODUCT.items():
            assertion.is_equals(k, v, resp[k])

    def test_delete_product(self):
        product_id = generator.generate_random_integer(1000, 5000)

        resp = product_service.delete_product(product_id)
        assertion.is_equals("Message", resp["message"], f"Product with id '{product_id}' not found")
