import os
from string import Template
from common.yaml_util import YamlUtil
import json
import pymysql

class DealTest:
    def getCases(self, host, user, password, database):
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





