import requests
from lxml import html
from urllib import request
import re

etree = html.etree
url = 'https://www.pearvideo.com/category_6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
page_text = response.text
tree = etree.HTML(page_text)
a_lis = tree.xpath('//*[@id="listvideoListUl"]/li/div/a')
for a in a_lis:
    href = 'https://www.pearvideo.com/'+a.xpath('./@href')[0]
    response = requests.get(url=href, headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    video_name = tree.xpath('//*[@id="poster"]/img/@alt')[0]+'.mp4'
    print(video_name)
    ex = 'srcUrl="(.*?)"'
    video_url = re.findall(ex, page_text)[0]
    request.urlretrieve(video_url, f'./videos/{video_name}')
    print(video_name, '下载成功！！！')
