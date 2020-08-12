import requests
from lxml import html


etree = html.etree
url = 'https://xueqiu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
p_lis = tree.xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[2]/div[1]/div/p')
for p in p_lis:
    print(p.xpath('./text()')[0])