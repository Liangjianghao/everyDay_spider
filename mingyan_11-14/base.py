#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/14 18:16
# @Author : L
# @Software: PyCharm
import os
import requests
from lxml import html
import time
def createFile(filePath):
    if os.path.exists(filePath):
        print('%s:存在'%filePath)
    else:
        try:
            os.mkdir(filePath)
            print('新建文件夹：%s'%filePath)
        except Exception as e:
            os.makedirs(filePath)
            print('新建多层文件夹：%s' % filePath)

def getDetailUrl(filePath,arrUrl):
    response=requests.get(arrUrl).text
    selector = html.fromstring(response)
    page_two = selector.xpath('//*[@id="p_left"]/div/ul[2]/li[3]/a/@href')[0]
    # print(page_two)
    page=1
    while 1:
        detailUrl=arrUrl+page_two[:-6]+'%s.html'%page
        print(detailUrl)
        response = requests.get(detailUrl)
        response.encoding = 'gb2312'
        selector = html.fromstring(response.text)
        detailList = selector.xpath('//*[@id="p_left"]/div/ul[1]/li/h2/a/@href')
        detailName = selector.xpath('//*[@id="p_left"]/div/ul[1]/li/h2/a/text()')
        print(len(detailList))
        if len(detailList)==0:
            break
        page+=1
        time.sleep(1)
        for index,articleUrl in enumerate(detailList):
            try:
                f=open('%s/%s.txt'%(filePath,detailName[index]),'w+')
                print(articleUrl)
                response=requests.get(url+articleUrl)
                response.encoding = 'gb2312'
                selector = html.fromstring(response.text)
                P_element = selector.xpath('//*[@id="p_left"]/div[1]/div[4]/p')
                for p in P_element:
                    if len(p.text)==1:
                        continue
                    else:
                        print(p.text)
                        f.write(p.text+'\n')
                f.close()
            except Exception as e:
                print(e)
                continue




url='https://www.geyanw.com/'
response=requests.get(url)
response.encoding = 'gb2312'
selector=html.fromstring(response.text)
myArr=selector.xpath('//*[@id="p_left"]/div/dl/dt/strong/a/@href')
nameArr=selector.xpath('//*[@id="p_left"]/div/dl/dt/strong/a/text()')
print(len(myArr))
for index,detail in enumerate(myArr):
    filePath=os.getcwd()+'/%s'%(nameArr[index])
    createFile(filePath)
    arrUrl=url+detail
    print(arrUrl)
    getDetailUrl(filePath,arrUrl)
    # break

# 代码冗余 有空优化 ufff bug