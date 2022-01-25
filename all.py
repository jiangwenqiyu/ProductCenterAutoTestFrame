import pytest
import os
import json
import shutil
from configs.EnvConfig import productEnv



# 修改报告内容
def alterRep():
    with open('./reports/widgets/summary.json', 'r') as f:
        data = json.loads(f.read())

    data['reportName'] = '商品中心测试报告'

    with open('./reports/widgets/summary.json', 'w') as f:
        f.write(json.dumps(data))

    with open('./reports/index.html', 'r') as f:
        data = f.read()
    pat = 'Allure Report'
    data = data.replace(pat, '鑫方盛测试中心')

    with open('./reports/index.html', 'w', encoding='utf-8') as f:
        f.write(data)



if __name__ == '__main__':
    productEnv('t4')   # 初始化环境参数
    pytest.main()
    os.system('allure generate ./report_temp -o ./reports --clean')
    alterRep()
    shutil.rmtree('./report_temp')
    os.mkdir('./report_temp')



