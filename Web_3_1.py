
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"html.parser")


nameList = bs0bj.findAll(text="the prince")
print(len(nameList))

allText = bs0bj.findAll(id="text")
print(allText[0].get_text())