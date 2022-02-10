#encoding=utf-8
import pytest
import os
import json
from configs.EnvConfig import productEnv
import requests
import datetime



# 修改报告内容
def alterRep():
    with open('reports/widgets/summary.json', 'r') as f:
        data = json.loads(f.read())

    data['reportName'] = '商品中心测试报告'

    with open('reports/widgets/summary.json', 'w') as f:
        f.write(json.dumps(data))

    with open('reports/index.html', 'r', encoding='utf-8') as f:
        data = f.read()
    pat = 'Allure Report'
    data = data.replace(pat, '鑫方盛测试中心')

    with open('reports/index.html', 'w', encoding='utf-8') as f:
        f.write(data)



if __name__ == '__main__':
    startTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    testEnvironment = 't4'
    productEnv(testEnvironment)   # 初始化环境参数
    pytest.main()
    os.system('allure generate ./report_temp -o ./reports -c ./reports')
    alterRep()
    endTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    word = '测试环境:{}\n开始时间:{}\n结束时间:{}\n查看测试报告:{}'.format(testEnvironment, startTime, endTime, 'http://192.168.0.129:7890/index.html')
    data = {
        'text':{'content':word},
        'msgtype':'text'
            }
    requests.post(productEnv.ding_token, json=data).json()





