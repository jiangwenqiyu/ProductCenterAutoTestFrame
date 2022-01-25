import os
from string import Template

import xlrd

from common.yaml_util import YamlUtil
import json
import pymysql

class DealTest:
    def getCasesFromDb(self, host, user, password, database):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        sql = ''' select s.jsonObj from product_test_functions_detail s
                where s.mainFunctionId = 1
        '''
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        con.close()
        t1 = list()
        for i in data:
            t1.append(json.loads(i[0]))

        return t1


    def getCasesFromExcel(self, name):
        allInfo = []
        work = xlrd.open_workbook('./testcases/{}'.format(name))
        sheet = work.sheet_by_name('sheet1')
        for i in range(1, sheet.nrows):
            temp = dict()
            temp['name'] = sheet.cell_value(i, 0)
            temp['path'] = sheet.cell_value(i, 1)
            temp['header'] = json.loads(sheet.cell_value(i, 2))
            temp['method'] = sheet.cell_value(i, 3)
            temp['data'] = json.loads(sheet.cell_value(i, 4))
            temp['dataType'] = sheet.cell_value(i, 5)
            temp['param'] = json.loads(sheet.cell_value(i, 6))
            temp['assert'] = json.loads(sheet.cell_value(i, 7))
            temp['save'] = sheet.cell_value(i, 8)
            if temp['save']:
                temp['save'] = json.loads(temp['save'])
            allInfo.append(temp)



        return allInfo





