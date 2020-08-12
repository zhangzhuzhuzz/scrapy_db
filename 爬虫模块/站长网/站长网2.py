from urllib import request
import requests
from lxml import html

etree = html.etree  # 类似于一个工具，把获取到的页面文本转化格式
url = 'http://sc.chinaz.com/jianli/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) compatible:MSIE 8.0'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
img_lis = tree.xpath('//li/a[@target="_blank"]/img')
for img in img_lis:
    src = img.xpath('@src')[0]
    filename = src.split('/')[-1]
    request.urlretrieve(src, f'./jianli/{filename}')
    print(filename, '下载成功！')
