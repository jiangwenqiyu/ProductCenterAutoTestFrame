import pytest
import json
import allure
from allure_commons._allure import Dynamic

from common.dealTestcases import DealTest
from common.requestPackage import RequestSend
from common.yaml_util import YamlUtil


def getInfo():
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
    host = ''
    token = ''
    db_host = ''
    db_user = ''
    db_pass = ''
    db_database = ''

    @allure.story('获取环境信息')
    def test_getEnv(self):
        data = YamlUtil().read_yaml('envConfig.yml', './configs/')['fangzhen']
        TestBasicQuery.host = data['host']
        TestBasicQuery.token = data['token']
        TestBasicQuery.db_host = data['db_link']
        TestBasicQuery.db_user = data['db_user']
        TestBasicQuery.db_pass = data['db_pass']
        TestBasicQuery.db_database = data['db_database']



    # @pytest.mark.parametrize('info', YamlUtil().read_yaml('修改分类.yml')['teststeps'])
    @allure.story('基础接口探活测试')
    @pytest.mark.parametrize('info', DealTest().getCases(**getInfo()))
    def test_query(self, info):

        '''查询、修改、审批分类'''
        Dynamic.title(info['name'])

        method = info['method'].lower()
        url = TestBasicQuery.host + info['path']
        header = info['header']
        header['cookie'] = 'uc_token={}'.format(TestBasicQuery.token)
        data = info['data']
        param = info['param']

        print(info['name'], method, url, TestBasicQuery.host)

        with allure.step('请求地址:{}\n请求参数:{}\n{}\n'.format(url, data, param)):
            res = self.requests.request(method, url, header, data = data, params = param)

        with allure.step('返回参数:{}'.format(res.text)):
            self.requests.myLog.debug('返回值: {}'.format(res.text))
            assert info['validate'] == res.text


    # @pytest.mark.parametrize('info', YamlUtil().read_yaml('test.yml'))
    # def test_aa(self, info):
    #     print(info)
    #     # info['url'] = 'aaa'






