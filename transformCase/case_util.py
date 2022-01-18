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
            temp = dict()


            url = obj['request']['url']
            path = ''
            for i in url.split('?')[0].split('/')[3:]:
                path += '/' + i

            method = obj['request']['method']

            req_data = obj['request']['postData'].get('text')
            if req_data:
                req_data = json.loads(req_data)
                temp['reqType'] = 'json'
            else:
                req_data = dict()
                temp['reqType'] = 'form'
                temp_data = obj['request']['postData'].get('params')
                for i in temp_data:
                    req_data[i['name']] = i['value']


            param = dict()
            for i in obj['request']['queryString']:
                param[i['name']] = i['value']

            header = dict()
            for i in obj['request']['headers']:
                if i['name'] == 'Accept' or i['name'] == 'Content-Type':
                    header[i['name']] = i['value']

            res = obj['response']['content']['text']

            temp['name'] = ''
            temp['path'] = path
            temp['header'] = header
            temp['data'] = req_data
            temp['param'] = param
            temp['method'] = method
            temp['validate'] = json.loads(res)

            self.cases.append(temp)
            # print(data)


    def addCase(self):
        with open('新建文本文档.txt', 'r', encoding='utf-8') as f:
            file = f.readlines()

        for i in range(len(file)):
            name = file[i].replace('\n', '')
            self.cases[i]['name'] = name


    def add_to_db(self):
        import pymysql
        import yaml
        from pymysql.converters import escape_string

        with open('../configs/envConfig.yml', 'r') as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
        print(file['fangzhen']['db_link'], file['fangzhen']['db_user'], file['fangzhen']['db_pass'])
        con = pymysql.connect(host=file['fangzhen']['db_link'], user=file['fangzhen']['db_user'], password=file['fangzhen']['db_pass'], database=file['fangzhen']['db_database'])
        cur = con.cursor()

        for i in self.cases:
            set = escape_string(json.dumps(i))
            sql = '''insert into product_test_functions_detail values(0,'{}','{}','{}',1,1,'')'''.format( i['name'], i['path'], set)
            cur.execute(sql)
        con.commit()
        cur.close()
        con.close()



o = CaseUtil()
o.harToJson('1.har')
o.addCase()
o.add_to_db()

