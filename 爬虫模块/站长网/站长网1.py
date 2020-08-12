import requests
from lxml import html
from urllib import request

url = 'http://sc.chinaz.com/tupian/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) compatible:MSIE 8.0'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

etree = html.etree  # 实例化etree对象
tree = etree.HTML(page_text)  # 转化page_text的格式

img_lis = tree.xpath('//div/a[@target="_blank"]/img')
for img in img_lis:
    alt = img.xpath('./@alt')[0]+'.jpg'
    src = img.xpath('./@src2')[0]
    request.urlretrieve(src, f'./images/{alt}')
    print(alt, '下载成功！')
