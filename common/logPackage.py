import logging

class MyLog(logging.Logger):
    def __init__(self, logName, level = logging.DEBUG, file = None):
        super().__init__(logName, level)

        fmt = '[%(levelname)s] [%(asctime)s] [%(funcName)s] %(message)s'
        formatter = logging.Formatter(fmt)

        consoleHandle = logging.StreamHandler()
        consoleHandle.setFormatter(formatter)
        self.addHandler(consoleHandle)

        if file:
            fileHandle = logging.FileHandler('./logInfo/{}'.format(file), encoding='utf-8')
            fileHandle.setFormatter(formatter)
            self.addHandler(fileHandle)




