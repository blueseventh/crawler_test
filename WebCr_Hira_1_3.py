#-*- coding: utf-8 -*-


import requests
import bs4

import sys
reload(sys)
sys.setdefaultencoding('utf-8')




endpoint = "http://apis.data.go.kr/B551182/mdlrtActionInfoService/getMdlrtActionByClassesStats?"
servicekey = "MSHdqGm%2BtYTAvwvKn%2BkajdvrMSOxJt840YrxsEGGfCHzkClo0BQjI33e%2B5QACU%2FrLNFuf60USAJPlHWA8GgZIg%3D%3D"
mdfeeCd = "P4552"
medTp = "2"
year = "2014"

paramset = "servicekey=" + servicekey + "&" + "mdfeeCd=" + mdfeeCd + "&" + "medTp=" + medTp + "&" + "year=" + year

url = endpoint + paramset
print("url : " + url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content,"html.parser")

counts = ["01","02","03"]
for count in counts:

    items = bs_obj.findAll("execfq"+count)

    data = []
    for item in items:
        item = item.text
        tag = item[0:len(item)-6].strip().replace(",","")
        tag = int(tag)
        data.append(tag)

    print(data)

    def caseno(yr):
        yr =[]
        for item in items:
            item = item.text
            tag = item[0:len(item) - 6].strip().replace(",", "")
            tag = int(tag)
            yr.append(tag)
        print(yr)


    caseno(year)

grades = bs_obj.findAll("item")



for gradeset in grades:
    gradesprint = gradeset.find("grade").text
    print gradesprint


tagset =[]
for gradetype in grades:
    tag = gradetype.find("grade")
    if type(tag) is str:
        print ("Yes")
    else:
        print ("No")

    print (tag)

    tagset.append(tag)
print (tagset)
