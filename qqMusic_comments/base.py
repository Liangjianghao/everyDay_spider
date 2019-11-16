#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/16 15:09
# @Author : L
# @Software: PyCharm
import requests
import json
import re
requests.packages.urllib3.disable_warnings()

f = open('jay.txt', 'w',encoding='utf-8')

def saveComments(commentsArr):
    for comment in commentsArr:
        nick=comment['nick']
        rootcommentcontent=comment['rootcommentcontent']
        compile=re.compile(r'\[em].*[/em].',re.S)
        c=re.sub(compile,'',rootcommentcontent)
        f.write(nick+'----'+c+'\n')

page=0
lasthotcommentid=''
while 1:
    url='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=160454710&loginUin=1808163167&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=237773700&cmd=8&needmusiccrit=0&pagenum=%s&pagesize=25&lasthotcommentid=%s&domain=qq.com&ct=24&cv=10101010'%(page,lasthotcommentid)
    print(url)
    response=requests.get(url,verify=False)
    jsno_data=json.loads(response.text)
    # print(jsno_data)
    commentsArr=jsno_data['comment']['commentlist']
    commenttotal=jsno_data['comment']['commenttotal']
    if len(commentsArr)==0:
        break
    # print('共有%s条评论'%commenttotal)
    saveComments(commentsArr)
    lasthotcommentid=commentsArr[-1]['rootcommentid']
    print(lasthotcommentid)
    page+=1
f.close()

