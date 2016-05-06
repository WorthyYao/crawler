# -*- coding:utf-8 -*-
from socket import error as SocketError
import urllib
import time
import urllib2
import re

#处理页面标签类
class Tool:
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将nbsp标签给删除
    removeLabel =re.compile('&nbsp;')
    #将文章来源给剔除
    removeSource =re.compile('来源.*')
    def replace(self,x):
        x = re.sub(self.replacePara,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeLabel,"",x)
        x = re.sub(self.removeSource,"",x)
        return x.strip()

class HY:
    def __init__(self,url):
        url=url
    def start(self):
        request=urllib2.Request(url)
        try:
            response=urllib2.urlopen(request)
        except SocketError as e:
            pass # Handle error here.

        try:
            pattern = re.compile('<div class="banner02 o_c_content01.*?>(.*?)</div>',re.S)
            result = re.search(pattern,response.read().decode('utf-8'))
        except:
            pass
        try:
            if result:
                contents=result.group(1).encode('utf-8')
                contents=Tool().replace(contents)
                f.write(contents)
                f.write('\n')
                print("spider",i)
            else:
                print i
        except:
            pass
f=open('航运信息.txt','w+')
for i in range(60000,80100):
    url='http://www.cnhangyun.com/news/article/info/id/'+str(i)
    hy=HY(url)
    hy.start()