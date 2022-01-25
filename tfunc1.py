import re
import json

saveValue = {
    '新增':{'uuid':{'idd':789}, 'iii':'草鸡巴'},

     '草':{'777':999}
}

def parseData(data):
    data = json.dumps(data, ensure_ascii=False)
    pat = '#(.*?)#'
    r = re.findall(pat, data)
    print(r)
    if r:
        for i in r:
            d = i.split('.')
            key = d[0]
            value = saveValue[key][d[1]]
            if len(d)>= 3:
                for x in range(2,len(d)):
                    value = value[d[x]]
            data = data.replace('#{}#'.format(i), str(value))
        return data

    else:
        return data


a = {"itemid": '#新增.uuid.idd#', "iii":"2"}

b = parseData(a)
print(b)












