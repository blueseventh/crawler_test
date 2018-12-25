import requests
from urllib.parse import urlparse

keyword ="강남역"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +"&display=100"
result = requests.get(urlparse(url).geturl(),
         headers ={"X-Naver-Client-Id":"Qp3GRPfTmgOSpYqDCG1j",
                   "X-Naver-Client-Secret":"RmVzlN2JVR"})

json_obj = result.json()
for item in json_obj['items']:
    print(item['title'].replace("<b>","").replace("</b>",""),
          item['link'])


#print(json_obj['display'])
#print(json_obj['start'])
#print(len(json_obj['items']))