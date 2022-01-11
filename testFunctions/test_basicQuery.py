import pytest
import json

from common.requestPackage import RequestSend
from common.yaml_util import YamlUtil


class TestBasicQuery:

    requests = RequestSend()

    @pytest.mark.parametrize('info', YamlUtil().read_yaml('修改分类.yml')['teststeps'])
    def test_query(self, info):
        method = info['request']['method'].lower()
        url = info['request']['url']
        header = info['request']['headers']
        header['cookie'] = 'uc_token=62d031124c47483da282849da1955475'
        data = None
        param = None
        for key in info['request']:
            if key == 'json':
                data = json.dumps(info['request']['json'])
            elif key == 'data':
                data = info['request']['data']
            elif key == 'params':
                param = info['request']['params']


        res = self.requests.request(method, url, header, data = data, params = param)
        for val in info['validate']:
            for k in val:
                if k == 'eq':
                    assert res.json()[val[k][0]] == val[k][1]
                elif k == 'in':
                    assert val[k][0] in res.text



