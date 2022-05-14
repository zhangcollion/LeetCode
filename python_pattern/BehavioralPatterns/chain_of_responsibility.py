from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request):
        "------------------"


class ConcreteHandler0(Handler):
    @staticmethod
    def check_range(request):
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True
        return None

class ConcreteHandler1(Handler):
    @staticmethod
    def check_range(request):
        if request > 10:
            print(f"request {request} handle in handler 1")
            return True
        return None


## 结束分支
class FallbcakHandler(Handler):
    @staticmethod
    def check_range(request):
        print("end of chain-------------")
        return False


## chain_of_responsibility
a = ConcreteHandler0(ConcreteHandler1(FallbcakHandler()))
for request in [1,2,12,334,34,2,1,34,2,33,-1,11]:
    a.handle(request)