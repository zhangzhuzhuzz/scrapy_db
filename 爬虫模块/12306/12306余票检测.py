import requests

city = {
    '北京': 'BJP',
    '重庆': 'CQW',
    '上海': 'SHH',
    '保定': 'BDP',
    '临城': 'UUP',
}

from_station = input('请输入出发地：').strip()
to_station = input('请输入目的地：').strip()
train_date = input('请输入日期（yyyy-mm-dd）：').strip()

url = 'https://kyfw.12306.cn/otn/leftTicket/query'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Cookie': '_uab_collina=159464857130558843784503; JSESSIONID=CF6926324E3FF149F63B5406B2937A28; BIGipServerotn=300941834.64545.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u4E34%u57CE%2CUUP; _jc_save_toStation=%u4FDD%u5B9A%2CBDP; _jc_save_fromDate=2020-07-14; _jc_save_toDate=2020-07-13; _jc_save_wfdc_flag=dc; RAIL_EXPIRATION=1594913835805; RAIL_DEVICEID=mnouLZdUcyUVGMvW-L_-aUaxguZw-yK3riuuRD4xmIfekcPjdg9FdwPCwGn8nnHP3v8sqt3CmcyItwDPg5huBYfXHfAsoLDXJRcGpV_0uZgzAFv-pbe7epOnKPn1LtDeh8-P0WZMEHDy2OqSxe6yBwZjAZrUs8hh'
}
params = {
    'leftTicketDTO.train_date': train_date,
    'leftTicketDTO.from_station': city[from_station],
    'leftTicketDTO.to_station': city[to_station],
    'purpose_codes': 'ADULT'
}
response = requests.get(url=url, headers=headers, params=params)
response.encoding = 'utf-8'
page_text = response.text
print(page_text)

# ajax异步请求，看到页面的url没有刷新，但是页面进行了刷新或者局部的刷新（比如登录注册界面、查询信息界面），那么这一定是ajax异步请求
# 从抓包工具的network里面的XHR中可以看到ajax异步请求的信息
