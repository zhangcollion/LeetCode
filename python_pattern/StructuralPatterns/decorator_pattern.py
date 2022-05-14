# The loggers all perform real output.
import sys


class FileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

class LogFilter:
    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger

    def log(self, message):
        print(self.pattern)
        if self.pattern in message:
            self.logger.log(message)

log1 = FileLogger(sys.stdout)
log2 = LogFilter('Error', log1)

# log1.log('Noisy: this logger always produces output')
# log2.log("asdddddddddddd asd Error")

log3 = LogFilter("warning", log2)
log3.log("dfsd asdd asd warning")
print("*"*20)
log3.log("dfsd asdd asd Error")
print("-"*20)
log3.log("dfsd asdd asd Error and warning")


