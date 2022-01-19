import json

import jsonpath

import jmespath
t = {"retStatus":"1","retMessage":"","retData":{"pageShow":10,"nowPage":1,"totalNum":7363,"totalPage":737,"results":[{"uuid":"2100000034","oper":"6674","opeTime":"2022-01-18 10:04:29","delFlag":1,"createOper":"6535","createOpeTime":"2021-12-29 09:49:31","version":22,"operationNumber":None,"orgId":"1002N1100000000126VI","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"吸水袋","categoryNo":"99999","categoryType":"3","categoryNote":"防洪用品","fullpath":"001006001002003000000000000000000","parentUuid":"21037","parentUuidStr":"安防>防汛救灾>防洪排涝","position":1,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":5000.0,"isKey":"2","categoryProductType":"3","dangerousOrder":"","canUpdate":"2","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"安防>防汛救灾>防洪排涝>吸水袋","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"30000","oper":"6674","opeTime":"2022-01-14 11:23:07","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":32,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"安全带","categoryNo":"01010101","categoryType":"3","categoryNote":"","fullpath":"001005008001002000000000000000000","parentUuid":"21000","parentUuidStr":"劳保>防坠落>安全带及配件","position":1010101,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":0.0,"isKey":"1","categoryProductType":"3","dangerousOrder":None,"canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"劳保>防坠落>安全带及配件>安全带","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"30001","oper":"6674","opeTime":"2022-01-14 11:23:03","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":8,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"安全带配件","categoryNo":"01010102","categoryType":"3","categoryNote":"","fullpath":"001005008001003000000000000000000","parentUuid":"21000","parentUuidStr":"劳保>防坠落>安全带及配件","position":1010102,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":0.0,"isKey":"1","categoryProductType":"3","dangerousOrder":None,"canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"劳保>防坠落>安全带及配件>安全带配件","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"31350","oper":"6674","opeTime":"2021-12-10 15:39:06","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":7,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"充电式圆锯","categoryNo":"13010105","categoryType":"3","categoryNote":"ddd","fullpath":"001017001001005000000000000000000","parentUuid":"21417","parentUuidStr":"动力工具>电动工具>充电电动工具","position":13010105,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":0.0,"isKey":"1","categoryProductType":"2","dangerousOrder":"0","canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"动力工具>电动工具>充电电动工具>充电式圆锯","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"30033","oper":"6674","opeTime":"2021-12-10 12:20:11","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":9,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"雨衣","categoryNo":"01030401","categoryType":"3","categoryNote":"","fullpath":"001005006004001000000000000000000","parentUuid":"21009","parentUuidStr":"劳保>身体防护>雨具","position":1030401,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":0.0,"isKey":"1","categoryProductType":"3","dangerousOrder":None,"canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"劳保>身体防护>雨具>雨衣","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"33280","oper":"6674","opeTime":"2021-12-02 13:44:54","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":4,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"穿墙螺栓 梯形丝杆","categoryNo":"30050306","categoryType":"3","categoryNote":"","fullpath":"001032004003006000000000000000000","parentUuid":"22177","parentUuidStr":"土建材料>模板辅料>穿墙螺栓","position":30050306,"state":"1","reviewState":"2","isPriceSensitive":"1","isMetal":"2","batchOrderPrice":0.0,"isKey":"2","categoryProductType":"3","dangerousOrder":None,"canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"土建材料>模板辅料>穿墙螺栓>穿墙螺栓 梯形丝杆","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"34578","oper":"6674","opeTime":"2021-11-25 11:18:23","delFlag":1,"createOper":"-1","createOpeTime":"2021-10-27 11:05:05","version":4,"operationNumber":None,"orgId":"","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"壁挂炉","categoryNo":"43010101","categoryType":"3","categoryNote":"","fullpath":"001045003001001000000000000000000","parentUuid":"22461","parentUuidStr":"暖通>采暖设备>壁挂炉","position":43010101,"state":"1","reviewState":"2","isPriceSensitive":"2","isMetal":"2","batchOrderPrice":0.0,"isKey":"2","categoryProductType":"3","dangerousOrder":None,"canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"暖通>采暖设备>壁挂炉>壁挂炉","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"2100000020","oper":"-1","opeTime":"2021-11-23 17:52:18","delFlag":1,"createOper":"14380","createOpeTime":"2021-11-03 14:12:49","version":6,"operationNumber":None,"orgId":"1002N11000000000HS3X","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"泽林分类四","categoryNo":"88888888","categoryType":"1","categoryNote":"","fullpath":"001004001001001000000000000000000","parentUuid":"2100000018","parentUuidStr":"泽林分类一>泽林分类二>泽林分类三","position":0,"state":"2","reviewState":"2","isPriceSensitive":"1","isMetal":"1","batchOrderPrice":120.0,"isKey":"1","categoryProductType":"3","dangerousOrder":"","canUpdate":"2","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"泽林分类一>泽林分类二>泽林分类三>泽林分类四","haveRel":None,"levelNum":"4","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"2100000008","oper":"14047","opeTime":"2021-11-08 16:00:34","delFlag":1,"createOper":"14047","createOpeTime":"2021-11-08 16:00:34","version":1,"operationNumber":None,"orgId":"1002N11000000000HS3X","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"sc1","categoryNo":"sc1","categoryType":"1","categoryNote":"111","fullpath":"001001000000000000000000000000000","parentUuid":"systemUuid","parentUuidStr":"","position":0,"state":"1","reviewState":"2","isPriceSensitive":"","isMetal":"","batchOrderPrice":0.0,"isKey":"2","categoryProductType":"","dangerousOrder":"","canUpdate":"2","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"sc1","haveRel":None,"levelNum":"1","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None},{"uuid":"2100000010","oper":"14047","opeTime":"2021-11-08 16:00:29","delFlag":1,"createOper":"14047","createOpeTime":"2021-11-08 16:00:29","version":1,"operationNumber":None,"orgId":"1002N11000000000HS3X","sortName":"opeTime","sortType":"desc","menuId":None,"buttonId":None,"loginUserId":None,"hrDepartmentNumber":None,"hrAreaId":None,"areaNo":None,"mapCondition":{},"categoryName":"sc2","categoryNo":"sc2","categoryType":"1","categoryNote":"222","fullpath":"001002000000000000000000000000000","parentUuid":"systemUuid","parentUuidStr":"","position":0,"state":"1","reviewState":"2","isPriceSensitive":"","isMetal":"","batchOrderPrice":0.0,"isKey":"2","categoryProductType":"","dangerousOrder":"","canUpdate":"1","tagCategoryNames":None,"brandNames":None,"brandUuids":None,"productTemplateNames":None,"productTemplateUuids":None,"acceptItemUuids":None,"acceptItemNames":None,"listAcceptItems":None,"classificationUuids":None,"classificationNames":None,"productSceneCategoryUuids":None,"productSceneCategoryNames":None,"listQualificationTypes":None,"fullNames":"sc2","haveRel":None,"levelNum":"1","templateUuids":None,"firstCategoryNo":None,"firstCategoryUuid":None,"firstCategoryName":None,"secondCategoryNo":None,"secondCategoryUuid":None,"secondCategoryName":None,"thirdCategoryNo":None,"thirdCategoryUuid":None,"thirdCategoryName":None,"fourthCategoryNo":None,"fourthCategoryUuid":None,"fourthCategoryName":None,"subList":None,"parentCategoryNo":None}],"fromNum":0},"timestamp":0}


a = jsonpath.jsonpath(t, '$.retStatus')


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

a = jmespath.compile('book[*].category').search(tt)
a = jmespath.search('retStatus', t)

print(a)

import xlrd

w = xlrd.open_workbook('提取har文件.xlsx')
sheet = w.sheet_by_name('sheet1')
a = sheet.cell_value(1, 7)
print(json.loads(a), type(a))






