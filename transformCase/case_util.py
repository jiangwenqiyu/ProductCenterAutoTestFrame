#encoding=utf-8
import json
import requests
# import jsonpath



class CaseUtil:

    def __init__(self):
        self.cases = list()


    def harToJson(self, filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            data = json.loads(f.read())

        for obj in data['log']['entries']:
            url = obj['request']['url']
            path = ''
            for i in url.split('?')[0].split('/')[3:]:
                path += '/' + i
            print(path)

            method = obj['request']['method']
            req_data = obj['request']['postData']
            param = dict()
            for i in obj['request']['queryString']:
                param[i['name']] = i['value']

            header = dict()
            for i in obj['request']['headers']:
                if i['name'] == 'Accept' or i['name'] == 'Content-Type':
                    header[i['name']] = i['value']

            res = json.loads(obj['response']['content']['text'])




    def addCase(self):
        pass


CaseUtil().harToJson('1.har')
