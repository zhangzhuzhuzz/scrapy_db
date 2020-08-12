import requests
from bs4 import BeautifulSoup

url = 'https://www.diyifanwen.com/guoxue/gulienvchuan/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) compatible:MSIE 8.0'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'gb2312'
page_text = response.text
soup = BeautifulSoup(page_text, 'lxml')
a_lis = soup.select('#AListBox > ul > li > a')
for a in a_lis:
    print(a['title'])
    url = 'http:'+a['href']
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gb2312'
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')
    p_lis = soup.select('#ArtContent > p')
    for p in p_lis:
        print(p.text.replace(' ', ''))
