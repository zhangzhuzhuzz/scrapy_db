import requests


name = input('>>>').strip()
url = 'https://cn.bing.com/search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
params = {
    'q': name
}
response = requests.get(url=url, params=params, headers=headers)
page_text = response.text

with open('动态爬bing.html','w',encoding='utf-8') as f:
    f.write(page_text)