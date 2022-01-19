#encoding=utf-8
import json
import requests
import xlsxwriter



class CaseUtil:

    def __init__(self):
        self.cases = list()
        self.work = xlsxwriter.Workbook('提取har文件.xlsx')
        self.sheet = self.work.add_worksheet('sheet1')
        self.sheet.write(0,0,'路径')
        self.sheet.write(0,1,'请求头')
        self.sheet.write(0,2,'请求方法')
        self.sheet.write(0,3,'入参')
        self.sheet.write(0,4,'入参类型')
        self.sheet.write(0,5,'param')
        self.sheet.write(0,6,'断言')
        self.sheet.write(0,7,'主方法id')
        self.sheet.write(0,8,'描述')




    def harToJson(self, filename):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            data = json.loads(f.read())

        a = 1
        for obj in data['log']['entries']:

            path = ''
            header = dict()
            method = obj['request']['method']
            req_data = obj['request']['postData'].get('text')
            reqType = ''
            param = dict()



            url = obj['request']['url']
            for i in url.split('?')[0].split('/')[3:]:
                path += '/' + i


            if req_data:
                req_data = json.loads(req_data)
                reqType = 'json'
            else:
                req_data = dict()
                reqType = 'form'
                temp_data = obj['request']['postData'].get('params')
                for i in temp_data:
                    req_data[i['name']] = i['value']

            for i in obj['request']['queryString']:
                param[i['name']] = i['value']

            for i in obj['request']['headers']:
                if i['name'] == 'Accept' or i['name'] == 'Content-Type':
                    header[i['name']] = i['value']

            self.sheet.write(a,0,path)
            self.sheet.write(a,1,json.dumps(header))
            self.sheet.write(a,2,method)
            self.sheet.write(a,3,json.dumps(req_data))
            self.sheet.write(a,4,reqType)
            self.sheet.write(a,5,json.dumps(param))

            a += 1

        self.work.close()

CaseUtil().harToJson('1.har')