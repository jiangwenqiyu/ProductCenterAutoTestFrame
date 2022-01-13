import json
import jsonpath



class CaseUtil:

    def __init__(self):
        self.cases = list()


    def harToJson(self, filename):
        pass


    def addCase(self):
        pass



a = {'a':123, 'b':456, 'c':[{'d':999}, {'d':111}]}

ret = jsonpath.jsonpath(a, '$.c[*].d')
print(ret)
print(a)