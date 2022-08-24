class Assertion:
    @staticmethod
    def is_not_null(field, value):
        assert value is not None, f"{field} is Null!"

    @staticmethod
    def is_equals(key, value1, value2):
        assert value1 == value2, f"{key}s are not equal"
