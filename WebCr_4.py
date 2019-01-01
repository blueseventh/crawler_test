from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,includerUrl):
    includerUrl = urlparse(includerUrl).scheme+"://"+urlparse(includerUrl).netloc
    internalLinks = [ ]

    for link in bsObj.findAll("a",href=re.compile("^(/|."+includerUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith("/"):
                    internalLinks.append(includerUrl+link.attrs['href'])
                else :
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj,excludeUrl):
    externallinks =[ ]
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def getRandomExternalLink (startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.rendint(0,len(internalLinks)-1)])

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is:"+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://www.oreilly.com/")

