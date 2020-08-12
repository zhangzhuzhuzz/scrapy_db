import requests


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'  # xhr
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
for p in range(1, 9):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': p,
        'pageSize': '10',
    }

    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.json()
    for i in page_text['Table1']:
        print(i['storeName']+'餐厅', '地址:' + i['addressDetail'])
