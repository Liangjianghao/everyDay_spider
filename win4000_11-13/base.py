#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/13 17:11
# @Author : L
# @Software: PyCharm

import os
import requests
from lxml import html
import urllib
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

def downloadImg(title,url):
    newPath=imgPath+'/%s'%title
    createFile(newPath)
    response=requests.get(url).text
    selector=html.fromstring(response)
    pageNumber=selector.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[1]/em/text()')[0]
    print(pageNumber)
    for i in range(1,int(pageNumber)+1):
        pageUrl= url[:-5] + '_' + str(i) + url[-5:]
        # print(pageUrl)
        response=requests.get(pageUrl).text
        selector = html.fromstring(response)
        imgUrl = selector.xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/a/img/@src')[0]
        # print(imgUrl)
        title = title.replace('/', '-').replace(' ', '')
        imgDetailPath=newPath+'/%s_%s.jpg'%(title,i)
        urllib.request.urlretrieve(imgUrl, imgDetailPath)

imgPath = os.getcwd() + '/img'
createFile(imgPath)
page=1
while 1:
    url='http://www.win4000.com/zt/youxi_%s.html'%page
    response=requests.get(url).text
    # print(response)
    selector=html.fromstring(response)
    detailArr=selector.xpath('/html/body/div[4]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li/a')

    print(len(detailArr))
    if len(detailArr)==0:
        break
    for d in detailArr:
        url=d.xpath('@href')[0]
        print(url)
        title=d.xpath('p/text()')[0]
        print(title)
        downloadImg(title,url)
        # break
    page+=1
    # break
