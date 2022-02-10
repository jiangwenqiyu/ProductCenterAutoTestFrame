import re
import json
import jmespath
from allure_commons._allure import Dynamic
from configs.EnvConfig import productEnv
from common.requestPackage import RequestSend

requests = RequestSend()


def parseData(data, dataType, saveValue):
    # 正则表达式解析测试用例的变量参数, 同时判断入参卡类型是json还是formdata， formdata返回字典，json返回字符串
    data = json.dumps(data, ensure_ascii=False)
    pat = '#(.*?)#'
    r = re.findall(pat, data)
    if r:
        for i in r:
            d = i.split('.')
            key = d[0]
            value = saveValue[key][d[1]]
            if len(d)>= 3:
                for x in range(2,len(d)):
                    value = value[d[x]]
            data = data.replace('#{}#'.format(i), str(value))
    else:
        pass

    if dataType == 'json':
        data = json.loads(data)
        data = json.dumps(data)
    else:
        data = json.loads(data)

    return data



def excuteCases(info):
    ''' 发送请求 '''

    Dynamic.title(info['name'])   # 设置报告标题
    url = productEnv.host + info['path']  # 用例路径
    method = info['method'].lower()  # 用例方法
    header = info['header']  # 用例请求头
    header['cookie'] = f'uc_token={productEnv.token}'  # 添加token
    data = parseData(info['data'], info['dataType'], productEnv.saveValue)     # 解析用例入参
    param = info['param']

    res = requests.request(info['dataType'], info['assert'], method, url, headers = header, data = data, params = param)     # 使用封装的方法，执行请求

    # for i in info['assert']:           # 遍历所有断言
    #     assert jmespath.search(i['jmespath'], res.json()) == i['exp']

    if info['save']:                 # 判断是否有需要保存的数据
        productEnv.saveValue[info['name']] = jmespath.search(info['save']['jmespath'], res.json())

    return info['assert'], res
