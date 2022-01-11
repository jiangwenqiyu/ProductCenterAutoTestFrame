import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./report_temp -o ./reports --clean')




# from common.yaml_util import YamlUtil
#
# a = YamlUtil().read_yaml('修改分类.yml')
# for info in a['teststeps']:
#     print(info['request']['headers'])