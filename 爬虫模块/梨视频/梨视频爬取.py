import requests
from lxml import html
from urllib import request
import re

etree = html.etree
url = 'https://www.pearvideo.com/category_59'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
page_text = response.text
tree = etree.HTML(page_text)
div_tree = tree.xpath('//*[@id="listvideoListUl"]/li/div/a')
i = 0
for a in div_tree:
    href = "https://www.pearvideo.com/"+a.xpath('@href')[0]
    href_text = requests.get(url=href, headers=headers).text
    # print(href_text)
    ex = 'srcUrl="(.*?)"'
    mp = re.findall(ex,href_text)[0]
    i = i+1
    request.urlretrieve(mp,f'./videos/{i}{".mp4"}')
    print(i, '下载成功')

