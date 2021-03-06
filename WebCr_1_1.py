from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())


def getLinks(articleurl):
    html = urlopen("http://en.wikipedia.org"+articleurl)
    bsobj = BeautifulSoup(html, "html.parser")
    return bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) >0 :
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

