from utils.data.data_generator import DataGenerator as generator

PRODUCT = {
    "title": generator.generate_title(),
    "description": generator.generate_description(),
    "price": generator.generate_random_integer(1000, 2000),
    "rating": generator.generate_random_integer(1, 5),
    "stock": generator.generate_random_integer(100, 300)
}

PRODUCT_RESPONSE_BODY = {
    "products": dict,
    "total": int,
    "skip": int,
    "limit": int,
}
