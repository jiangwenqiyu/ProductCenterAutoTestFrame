import pytest
import json
import allure
from allure_commons._allure import Dynamic

from common.requestPackage import RequestSend
from common.yaml_util import YamlUtil

@allure.feature('商品基础-品类管理')
class TestBasicQuery:

    requests = RequestSend()

    # @allure.story('简简单单')
    @pytest.mark.parametrize('info', YamlUtil().read_yaml('修改分类.yml')['teststeps'])
    def test_query(self, info):
        '''查询、修改、审批分类'''
        Dynamic.title(info['title'])

        method = info['request']['method'].lower()
        url = info['request']['url']
        header = info['request']['headers']
        header['cookie'] = 'uc_token=e957c609b1554018ae97fe1dc86e9cf1'
        data = None
        param = None
        for key in info['request']:
            if key == 'json':
                data = json.dumps(info['request']['json'])
            elif key == 'data':
                data = info['request']['data']
            elif key == 'params':
                param = info['request']['params']

        with allure.step('请求地址:{}\n请求参数:{}\n{}\n'.format(url, data, param)):
            res = self.requests.request(method, url, header, data = data, params = param)

        with allure.step('返回参数:{}'.format(res.text)):
            self.requests.myLog.debug('返回值: {}'.format(res.text))
            for val in info['validate']:
                for k in val:
                    if k == 'eq':
                        assert res.json()[val[k][0]] == val[k][1]
                    elif k == 'in':
                        assert val[k][0] in res.text


    # @pytest.mark.parametrize('info', YamlUtil().read_yaml('test.yml'))
    # def test_aa(self, info):
    #     print(info)
    #     # info['url'] = 'aaa'






