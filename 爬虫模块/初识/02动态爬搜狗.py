import requests


name = input('>>>').strip()
url = 'https://www.sogou.com/web'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
params = {
    'query': name
}
response = requests.get(url=url, params=params, headers=headers)
page_text = response.text

with open('动态爬搜狗.html','w',encoding='utf-8') as f:
    f.write(page_text)