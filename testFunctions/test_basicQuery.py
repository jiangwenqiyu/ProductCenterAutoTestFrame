import pytest
import json
import allure
from allure_commons._allure import Dynamic
from common.loadCasesFromDb import DealTest
from common.requestPackage import RequestSend
from common.yaml_util import YamlUtil
import time
from configs.EnvConfig import productEnv
import jmespath


def getDbInfo():
    data = YamlUtil().read_yaml('envConfig.yml', './configs/')['fangzhen']
    temp = dict()
    temp['host'] = data['db_link']
    temp['user'] = data['db_user']
    temp['password'] = data['db_pass']
    temp['database'] = data['db_database']
    return temp


@allure.feature('基础页面接口查询')
class TestBasicQuery:

    requests = RequestSend()


    @allure.story('测试接口集')
    @pytest.mark.parametrize('info', DealTest().getExcel())
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_query(self, info):
        time.sleep(1)
        Dynamic.title(info['name'])

        method = info['method'].lower()
        url = productEnv.host + info['path']
        header = info['header']
        header['cookie'] = f'uc_token={productEnv.token}'
        reqType = info['dataType']
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
            for i in info['assert']:
                assert jmespath.search(i['jmespath'], res.json()) == i['exp']


@allure.feature('修改四级分类')
class TestAlterCate:
    requests = RequestSend()

    @allure.title('初始化清空待审核单据')
    def test_init(self):
        pass







































