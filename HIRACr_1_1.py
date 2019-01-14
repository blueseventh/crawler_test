from urllib.request import urlopen
from urllib.urlencode import quote_plus

url = 'http://apis.data.go.kr/B551182/mdlrtActionInfoService/getMdlrtActionByAreaStats'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'MSHdqGm%2BtYTAvwvKn%2BkajdvrMSOxJt840YrxsEGGfCHzkClo0BQjI33e%2B5QACU%2FrLNFuf60USAJPlHWA8GgZIg%3D%3D', quote_plus('ServiceKey') : '-', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('mdfeeCd') : 'P4552', quote_plus('medTp') : '2', quote_plus('year') : '2017' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)