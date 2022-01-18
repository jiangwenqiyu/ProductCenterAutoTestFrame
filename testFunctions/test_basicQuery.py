import pytest
import json
import allure
from allure_commons._allure import Dynamic

from common.loadCasesFromDb import DealTest
from common.requestPackage import RequestSend
from common.yaml_util import YamlUtil
import time

from configs.EnvConfig import productEnv


def getDbInfo():
    data = YamlUtil().read_yaml('envConfig.yml', './configs/')['fangzhen']
    temp = dict()
    temp['host'] = data['db_link']
    temp['user'] = data['db_user']
    temp['password'] = data['db_pass']
    temp['database'] = data['db_database']
    return temp


@allure.feature('基础接口探活测试')
class TestBasicQuery:

    requests = RequestSend()


    @allure.story('测试接口集')
    @pytest.mark.parametrize('info', DealTest().getCases(**getDbInfo()))
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_query(self, info):
        time.sleep(1)
        Dynamic.title(info['name'])

        method = info['method'].lower()
        url = productEnv.host + info['path']
        header = info['header']
        header['cookie'] = f'uc_token={productEnv.token}'
        reqType = info['reqType']
        if reqType == 'json':
            data = json.dumps(info['data'])
        else:
            data = info['data']
        param = info['param']


        with allure.step('请求地址:{}\n'.format(url)):
            pass
        with allure.step('请求参数:data:{}\nparam:{}\n'.format(data, param)):
            pass
        with allure.step('请求头:{}\n'.format(header)):
            res = self.requests.request(method, url, header, data = data, params = param)

        with allure.step('返回参数:{}'.format(res.text)):
            self.requests.myLog.debug('返回值: {}'.format(res.text))
            assert res.status_code == 200
            assert res.json()['retStatus'] == '1'









































