import requests
from bs4 import BeautifulSoup

URL = "https://naver.com"
res = requests.get(URL)
bs_obj = BeautifulSoup(res.content, "html.parser")

if_items = bs_obj.findAll("span",{"class":"td_mw"})

hrefs = [span.find("img")['href'] for span in if_items]

print(if_items)
