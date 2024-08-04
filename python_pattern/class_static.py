class Date:
    def __init__(self, day=0, month=0,year=0):
        self.day = day
        self.month = month
        self.year = year
        self.print_date()
    def print_date(self):
        print(f"{self.year}-{self.month}-{self.day}")

    @classmethod
    def create_date(cls, date_string):
        year, month, day = date_string.split("-")
        date = cls(day, month, year)
        return date

    @staticmethod
    def is_date_valid(date_string):
        year, month, day = date_string.split("-")
        return 0 < int(day) < 31 and 0< int(month) < 13

date1 = Date(14,5,2022)
 ## "2202-2-23"创建一个对象, 很明显会用到类中的初始化方法
date2 = Date.create_date("2022-02-23")

##判断一个字符数是否是一个有效的日期， 类的一个功能，不需要用到类中的数据等
## $$ 2222  ##
print(Date.is_date_valid("2202-022-03"))

## $$ 3333 ##

## $$ 4 ##


