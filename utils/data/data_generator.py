from faker import Faker


class DataGenerator:

    @staticmethod
    def generate_description():
        return Faker().paragraph(nb_sentences=5, variable_nb_sentences=False)

    @staticmethod
    def generate_title():
        return Faker().word()

    @staticmethod
    def generate_random_integer(min_int, max_int):
        return Faker().random.randint(min_int, max_int)
