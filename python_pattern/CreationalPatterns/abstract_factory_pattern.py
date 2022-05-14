from decimal import Decimal


def build_decimal(string):
    return Decimal(string.lstrip("$"))

class DecimalFactory(object):
    @staticmethod
    def build(string):
        return Decimal(string.lstrip("$"))


class Loader(object):
    @staticmethod
    def load(string, factory):
        string = string.rstrip(",")
        return [factory.build(item) for item in string.split(",")]

result = Loader.load("$$$$468.02, 655.23", DecimalFactory)
print(result)