## Abstractions
import sys


class Logger(object):
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.emit(message)

##改需求，不需要所有的log都显示，只显示带有关键字的
class KeyWordLogger(object):
    def __init__(self, pattern, handler):
        self.pattern = pattern
        self.handler = handler

    def log(self, messgae):
        if self.pattern in messgae :
            self.handler.emit(messgae)


class FileHandler:
    def __init__(self, file):
        self.file = file

    def emit(self, message):
        self.file.write(message+"\n")
        self.file.flush()

import sys
file_handler = FileHandler(sys.stdout)
logger = Logger(file_handler)
logger.log("dasdasdasd sadddasd asddddddd")

key_logger = KeyWordLogger("Error", file_handler)
key_logger.log("asd asda asd")
print("*"*20)
key_logger.log("Error asd asd key")