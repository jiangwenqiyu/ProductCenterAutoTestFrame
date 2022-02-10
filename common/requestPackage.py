import json

import requests
import allure
from common.logPackage import MyLog


class RequestSend:

    myLog = MyLog('testLog', file = 'autoTestLog.log')



    def request(self, dataType, assertions, method, url, **kwargs):
        log = list()
        log.append(method)
        log.append(url)
        log.append(kwargs)

        try:

            data = kwargs.get('data')
            if dataType == 'json':
                data = json.loads(data)


            with allure.step('请求地址:{}\n'.format(url)):
                pass

            with allure.step('请求参数:data:{}\nparam:{}\n'.format(data, kwargs.get('params'))):
                res = requests.request(method, url, **kwargs)
                assert res.status_code == 200, '状态码错误'

            with allure.step('返回参数:{}'.format(res.text)):
                log.append('返回值:{}'.format(res.text))
                self.myLog.debug(log)

            with allure.step('断言依据:{}'.format(assertions)):
                pass

            return res

        except Exception as e:

            log.append(e)
            self.myLog.warning(log)
            raise e








