class Catalog:
    def __init__(self, param):
        self._static_method_choices = {
            "param1":self._static_method1,
            "param2":self._static_method2
        }
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError(f"Invalid Value for param: {param}")
    @staticmethod
    def _static_method1():
        print("---------1---------")

    @staticmethod
    def _static_method2():
        print("---------2---------")

    def main_method(self):
        self._static_method_choices[self.param]()

a = Catalog("param2")
a.main_method()