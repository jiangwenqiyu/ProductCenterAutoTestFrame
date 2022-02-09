import re
import json

import requests

url = 'http://product.t4.xinfangsheng.com/sysback/template/producttemplateattrvaluecategory/baseUpdate?menuId=218&buttonId=3'
header = {'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json;charset=UTF-8',
          'Cookie': 'uc_token=78483cd4925641d68c6ceb73f488c1fe'}
data = {"uuid":"2100003092","oper":"6674","opeTime":"2022-01-25 15:02:57","delFlag":1,"createOper":"112130","createOpeTime":"2021-10-24 11:11:10","version":6,"operationNumber":None,"orgId":"1002N11000000000HS44","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"脚本御用属性值分类"}

res = requests.post(url, headers = header, json = data).json()
print(res)










