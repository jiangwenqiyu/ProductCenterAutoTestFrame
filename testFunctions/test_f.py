import pytest
import allure

@allure.title('类测试')
class TestSend:

    @allure.title('测试')
    def test_01(self):
        '''测试用例'''
        print(1)



