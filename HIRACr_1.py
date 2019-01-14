from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://apis.data.go.kr/B551182/mdlrtActionInfoService/getMdlrtActionByClassesStats?mdfeeCd=p4552&medTp=2&year=2014&ServiceKey=MSHdqGm%2BtYTAvwvKn%2BkajdvrMSOxJt840YrxsEGGfCHzkClo0BQjI33e%2B5QACU%2FrLNFuf60USAJPlHWA8GgZIg%3D%3Dhttp://apis.data.go.kr/B551182/mdlrtActionInfoService/getMdlrtActionByClassesStats?mdfeeCd=p4552&medTp=2&year=2014&ServiceKey=MSHdqGm%2BtYTAvwvKn%2BkajdvrMSOxJt840YrxsEGGfCHzkClo0BQjI33e%2B5QACU%2FrLNFuf60USAJPlHWA8GgZIg%3D%3D")

bsObj= BeautifulSoup(html,"html.parser")

print(bsObj)






