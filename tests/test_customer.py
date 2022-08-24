import pytest

from service.products.products_service import ProductService as product_service
from service.carts.carts_service import CartsService as carts_service


class TestProducts:
    """Products tests - """

    @pytest.mark.usefixtures('run_services')
    def test_get_customers(self):
        product_ids = list()
        matched_carts_user_ids = list()

        product_list = product_service.get_products()["products"]

        products = list(
            filter(lambda x: x["category"] == "laptops", list(filter(lambda x: x["price"] <= 1500, product_list))))

        for i in products:
            product_ids.append(i["id"])

        carts = carts_service.get_carts()

        for i in product_ids:
            for j in carts:
                item = list(filter(lambda x: x["id"] == i, j['products']))
                if len(item) != 0:
                    matched_carts_user_ids.append(j['userId'])