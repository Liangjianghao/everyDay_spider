#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/15 19:09
# @Author : L
# @Software: PyCharm


import scrapy
import json
from scrapy.http import Request
from ac_up.items import AcUpItem
import random
user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

class Myspider(scrapy.Spider):
    name='ac_up'
    allowed_domains=['https://apipc.app.acfun.cn']
    base_url='https://apipc.app.acfun.cn/v2/user/content/profile?app_version=5.10.2&market=appstore&origin=ios&resolution=750x1334&sys_name=ios&sys_version=12.0&userId=1'

    def start_requests(self):
        for x in range(1, 100000):
            ua = random.choice(user_agent_list)
            self.headers = {
                'User-Agent': ua,
                'deviceType': 0
            }
            url = 'https://apipc.app.acfun.cn/v2/user/content/profile?app_version=5.10.2&market=appstore&origin=ios&resolution=750x1334&sys_name=ios&sys_version=12.0&userId=%s' % x
            yield Request(url,headers=self.headers,callback=self.parse)
    def parse(self,response):
        try:
            result = json.loads(response.text)
            userid=result['vdata']['userId']
            userName=result['vdata']['username']
            fenceNum=result['vdata']['followed']
            bananaGold=result['vdata']['bananaGold']
            userImg=result['vdata']['userImg']

            print('正在抓取第%s条数据:%s,%s,%s,%s'%(userid,userid,userName,fenceNum,bananaGold))
            # iterm=AcUpItem()
            # iterm['userId']=userid
            # iterm['userImg']=userImg
            # iterm['userName']=userName
            # iterm['fenceNum']=fenceNum
            # iterm['bananaGold']=bananaGold
            # yield iterm
        except Exception as e:
            print('parseException:%s'%e)
            print(result)