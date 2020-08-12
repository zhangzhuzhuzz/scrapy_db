import requests
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; compatible:MSIE 7.0'
}
data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': '',
}
response = requests.post(url=url, headers=headers, data=data)
page_text = response.json()
# print(page_text)
for i in page_text['list']:
    url2 = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    data2 = {
        'id': i['ID']
    }
    response2 = requests.post(url=url2, headers=headers, data=data2)
    page_text2 = response2.json()
    for j in page_text2:
        if page_text2[j] != '':
            print(page_text2[j])
    print('~'*20)

