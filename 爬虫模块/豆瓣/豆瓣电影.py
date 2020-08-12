import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '13',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '10',
}
response = requests.get(url=url, params=params, headers=headers)
for i in response.json():
    print(i['title']+i['score'])
