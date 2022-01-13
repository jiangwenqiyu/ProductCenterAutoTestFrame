import os
from string import Template
from common.yaml_util import YamlUtil
import json


class DealTest:

    def getTestcases(self, data, **kwargs):
        if len(kwargs) == 0:
            data = Template(json.dumps(data)).safe_substitute(os.environ)
        data = json.loads(data)
        return data



    def get(self):
        os.environ['name'] = '测试'
        os.environ['fuck'] = '我草'
        t = {'a':{'b':123}}
        y  = YamlUtil().read_yaml('test.yml')
        print(t[y['step'][0]['temp'][0]])
        print(self.getTestcases(y))


DealTest().get()



