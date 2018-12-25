import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Chrome/66.0.3359.181'}

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url, headers=headers)

bs_obj = BeautifulSoup(result.content, "html.parser")

ul = bs_obj.find("ul",{"class":"prdList column5"})
boxes = ul.findAll("div",{"class":"box"})

def get_product_info(box):
    ptag = box.find("p",{"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")

    name = spans_name[1].text
    price = spans_price[1].text

    atag = box.find("a")
    link = atag['href']

    return {"name":name, " price":price, "link":link}


for box in boxes:
    product_info = get_product_info(box)
    print(product_info)