class OddNumbers(object):
    def __init__(self,maximum):
        self.maximum = maximum
    def __iter__(self):
        return OddIterator(self)

    def __next__(self):
        print(f"-----{0}---------")


class OddIterator(object):
    def __init__(self, contrainer):
        self.contrainer = contrainer
        self.n = -1

    def __next__(self):
        print(f"-----{self.n}---------")
        self.n += 2
        if self.n > self.contrainer.maximum:
            raise StopIteration
        return self.n

    ## 实现了__iter__的对象可迭代
    # for 循环时，先调用__iter__, 获得可迭代器
    # 然后循环过程中循环调用__next__()函数
    def __iter__(self):
        print("--------------")
        # return self.contrainer
        return self

for i in OddIterator(OddNumbers(7)):
    print(i)

# t = OddIterator(OddNumbers(7))
# for i in range(3):
#     print(t.__next__())