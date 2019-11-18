#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/18 18:25
# @Author : L
# @Software: PyCharm
import requests
import json
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()

f=open('163.txt','w+',encoding='utf-8')
def get_artists(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=headers,verify=False)
    soup = BeautifulSoup(r.text, 'lxml')
    for artist in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        artist_name = artist.string
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        try:
            f.write(artist_id+'----'+artist_name+'\n')
        except Exception as msg:
            print(msg)

idList = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
initialList = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
for i in idList:
    for j in initialList:
        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        print(url)
        get_artists(url)
f.close()
