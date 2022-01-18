import pytest
import allure

from all import productEnv
from common.requestPackage import RequestSend


@allure.feature('数据初始化')
class TestInitData:
    request = RequestSend()


    @allure.story('清空四级类待审核')
    def test_cate_wait_check(self):
        pass






