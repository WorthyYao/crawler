# -*- coding:utf-8 -*-
import re
import urllib2



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


request=urllib2.Request('http://www.cnhangyun.com/news/article/info/id/72331.html')
response=urllib2.urlopen(request)
result=response
# print response.read()
pattern=re.compile('<div class="banner02 o_c_content01.*?>.*?</div>',re.S)
contents=re.search(pattern,response.read().decode('utf-8'))
print Tool().replace(contents.group(0).encode('utf-8'))
