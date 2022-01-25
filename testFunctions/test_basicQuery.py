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
@pytest.mark.skip
class TestBasicQuery:

    # @allure.story('测试接口集')
    @pytest.mark.parametrize('info', DealTest().getCasesFromExcel('基础界面查询接口.xlsx'))
    @pytest.mark.flaky(reruns=2, reruns_delay=0)
    def test_query(self, info):
        common_functions.excuteCases(info)



@allure.feature('修改验收事项')
@pytest.mark.run(order = 2)
class TestAcceptItem:

    @pytest.mark.parametrize('info', DealTest().getCasesFromExcel('修改验收事项.xlsx'))
    def test_init(self, info):
        common_functions.excuteCases(info)










































