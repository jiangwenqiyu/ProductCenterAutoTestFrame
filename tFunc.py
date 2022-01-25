import json
import jmespath


tt = {
    "store": {
    "book": [
        { "category": "reference",
          "author": "Nigel Rees",
          "title": "Sayings of the Century",
          "price": 8.95
          },
        { "category": "fiction",
          "author": "Evelyn Waugh",
          "title": "Sword of Honour",
          "price": 12.99
          },
        { "category": "fiction",
          "author": "Herman Melville",
          "title": "Moby Dick",
          "isbn": "0-553-21311-3",
          "price": 8.99
          },
        { "category": "fiction",
          "author": "J. R. R. Tolkien",
          "title": "The Lord of the Rings",
          "isbn": "0-395-19395-8",
          "price": 22.99
          }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}


# tt = {"retStatus":"1","retMessage":"","retData":"2100003043","timestamp":0}

a = jmespath.search('store.book[0].price', tt)
print(a)



import xlrd
import pymysql
from _pydecimal import Decimal, Context, ROUND_HALF_UP


def openEx(name):
    work = xlrd.open_workbook(name)
    sheet = work.sheet_by_name('审核模板')
    return sheet


def ttt():
    con = pymysql.connect(host='192.168.0.31', user = 'usercenter', password = 'usercenter123!', database = 'xfs_product_70w', port = 3307)
    cur = con.cursor()

    s1 = openEx('导出审核数据.xlsx')
    e1 = dict()
    for i in range(1, s1.nrows):
        sku = s1.cell_value(i, 10)
        supply = s1.cell_value(i, 1)
        cityName = s1.cell_value(i, 7)
        cost = s1.cell_value(i, 15)

        sql = ''' select s1.mainUnitCostPrice from product_supply_price s1
                left join product_supply_area s2 on s2.saleCityUuid = s1.templateCityUuid and s1.supplyUuid = s2.supplyUuid and s1.skuNo = s2.skuNo
                where s2.templateCityName = '{}' and s1.supplyUuid = '{}' and s1.skuNo = '{}' '''.format(cityName, supply, sku)
        cur.execute(sql)
        data = cur.fetchall()[0][0]

        assert Context().create_decimal(str(data)) == Context().create_decimal(cost), 'sku:{}, 供应商:{}, 城市:{}, 数据库:{},表单:{}'.format(sku, supply, cityName, data, cost)

# ttt()




