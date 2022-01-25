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
    Dynamic.title(info['name'])

    url = productEnv.host + info['path']
    method = info['method'].lower()
    header = info['header']
    header['cookie'] = f'uc_token={productEnv.token}'
    data = parseData(info['data'], info['dataType'], productEnv.saveValue)
    param = info['param']

    res = requests.request(method, url, headers = header, data = data, params = param)

    for i in info['assert']:
        assert jmespath.search(i['jmespath'], res.json()) == i['exp']

    if info['save']:
        productEnv.saveValue[info['name']] = jmespath.search(info['save']['jmespath'], res.json())

