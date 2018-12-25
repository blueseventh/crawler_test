import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Chrome/66.0.3359.181'}


url = "https://bp.eosgo.io/listing/eos-germany/"
result = requests.get(url, headers=headers)

bs_obj = BeautifulSoup(result.content,"html.parser")

print(bs_obj)