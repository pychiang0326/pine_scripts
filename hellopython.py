# To change this template, choose Tools | Templates
# and open the template in the editor.
import re
import datetime


def date2str(startDay):
    yyyy = startDay[0:4]
    mm = startDay[5:7]
    dd = startDay[8:10]
    strdate = yyyy + mm + dd
    return strdate


def print_dict(p_dict):
    for key1, value1 in p_dict.items():
        print(key1 + ':')
        list = []
        # p_dict[key1] = {key2:value2}
        for i in iter(p_dict[key1]):  # get key2 iterator in p_dict{}
            # print(i)
            list.append(i)
        list.sort()  # sort by key2
        for i in list:
            value2 = p_dict[key1][i]
            print(i + ':' + str(value2))
        """
        for key2,value2 in value1.items():
            print(key2 + ':' + str(value2))"""


def append_dict(fileName):
    # f = open("D:\\test\\venation_20100304mt.txt")
    f = open(fileName)
    try:
        for line in f:
            # print(line)
            m = re.findall("\d+\/\d+\/\d+", line)
            if (m):
                key1 = m[0]
                # print(key1)
            if (key1 not in p_dict):
                p_dict[key1] = {}
            m = re.findall("[A-Z]", line)
            if (m):
                key2 = m[0]
                # print(key2)
                if (key2 not in p_dict[key1]):
                    p_dict[key1][key2] = 1
                else:
                    p_dict[key1][key2] += 1
    finally:
        f.close()


startDay = datetime.date(2010, 3, 4)
endDay = datetime.date(2010, 3, 10)
endDay = endDay + datetime.timedelta(1)

p_dict = {}
while startDay <= endDay:
    currenDateStr = date2str(str(startDay))
    # print(currenDateStr)
    # fileName="D:\\test\\venation_"+currenDateStr+"mt.txt"
    fileName = "C:\\test\\venation_" + currenDateStr + "mt.txt"
    append_dict(fileName)
    startDay = startDay + datetime.timedelta(1)
# print dictionary
print_dict(p_dict)
