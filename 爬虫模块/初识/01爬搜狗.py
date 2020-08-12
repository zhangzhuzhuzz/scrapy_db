import requests

url = 'https://www.sogou.com/'
response = requests.get(url=url)
page_text = response.text

with open('搜狗.html','w',encoding='utf-8') as f:
    f.write(page_text)