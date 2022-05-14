class DiscountStrategyValidator:
    @staticmethod
    def valid(obj, value_func):
        try:
            if obj.price - value_func(obj) < 0:
                raise ValueError(f"Discount cannot be applied due to negative price resulting. {value_func.__name__}")
        except ValueError as ex:
            print(str(ex))
            return False
        else:
            return True

    def __set_name__(self, owner, name):
        self.privat_name = f"_{name}"

    def __set__(self, obj, value):
        if value and self.valid(obj, value):
            setattr(obj, self.privat_name, value)
        else:
            setattr(obj, self.privat_name, None)

    def __get__(self, obj, objtype=None):

        return getattr(obj, self.privat_name)


class Order:
    ##当类 Order 被定义的时候 在定义完后调用__set_name__
    ## 会回调__set_name__ 函数，创建一个DiscountStrategyValidator的实例
    # owner表示 Order这个class, name 为实例名“discount_strategy”
    discount_strategy = DiscountStrategyValidator()

    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def apply_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount


def ten_discount(order):
    return order.price * 0.1


def five_discount(order):
    return order.price * 0.5 + 100


order1 = Order(0, discount_strategy=five_discount)
print(order1.apply_discount())
