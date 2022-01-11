import requests

from common.logPackage import MyLog


class RequestSend:

    myLog = MyLog('testLog', file = 'autoTestLog.log')



    def request(self, method, url, header, **kwargs):
        log = list()
        log.append(method)
        log.append(url)
        log.append(kwargs)
        self.myLog.debug(log)
        res = requests.request(method, url, headers = header, **kwargs)
        return res






