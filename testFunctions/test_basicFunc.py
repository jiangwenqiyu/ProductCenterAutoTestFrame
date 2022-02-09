import pytest
import json
import allure
from allure_commons._allure import Dynamic
from common.loadCasesFromDb import DealTest
from common.requestPackage import RequestSend
from configs.EnvConfig import productEnv
import jmespath
import re
from common import common_functions


@allure.feature('基础页面接口查询')
@pytest.mark.run(order = 1)
class TestBasicQuery:

    # @allure.story('测试接口集')
    @pytest.mark.parametrize('info', DealTest().getCasesFromExcel('基础界面查询接口.xlsx'))
    @pytest.mark.flaky(reruns=2, reruns_delay=0)
    def test_query(self, info):
        ass, res = common_functions.excuteCases(info)
        for i in ass:
            assert jmespath.search(i['jmespath'], res.json()) == i['exp']



@allure.feature('修改验收事项')
@pytest.mark.run(order = 2)
class TestAcceptItem:

    @pytest.mark.parametrize('info', DealTest().getCasesFromExcel('修改验收事项.xlsx'))
    def test_run(self, info):
        common_functions.excuteCases(info)


@allure.feature('属性管理')
@pytest.mark.run(order = 3)
class TestAttributionManage:

    def test_run(self):
        pass


@allure.feature('四级类')
@pytest.mark.run(order = 4)
class TestCate:

    def test_run(self):
        pass






































