import requests
from urllib import request
import re

url = 'http://www.521609.com/daxuexiaohua/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
response = requests.get(url=url, headers=headers).text
ex = '<li>.*?<img src="(.*?)" width=.*?</li>'
img_list = re.findall(ex, response, re.S)
for i in img_list:
    img_name = i.split('/')[-1]
    # http://www.521609.com/uploads/allimg/140717/1-140GF92J7-lp.jpg
    img_url = 'http://www.521609.com'+i
    img_path = './花/'+img_name
    request.urlretrieve(img_url, img_path)
    print(img_name+'下载成功')
