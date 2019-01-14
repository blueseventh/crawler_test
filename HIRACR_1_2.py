import requests
import bs4

endpoint = "http://apis.data.go.kr/B551182/mdlrtActionInfoService/getMdlrtActionByClassesStats?"
servicekey = "MSHdqGm%2BtYTAvwvKn%2BkajdvrMSOxJt840YrxsEGGfCHzkClo0BQjI33e%2B5QACU%2FrLNFuf60USAJPlHWA8GgZIg%3D%3D"
mdfeeCd = "P4552"
medTp = "2"
year = "2013"

paramset = "servicekey=" + servicekey + "&" + "mdfeeCd=" + mdfeeCd + "&" + "medTp=" + medTp + "&" + "year=" + year

url = endpoint + paramset
print("url : " + url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")
for item in items:
    tagged_item = item.find("")
    print(tagged_item)

