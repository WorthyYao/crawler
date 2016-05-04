# coding=utf-8

import urllib2
import re


content = urllib2.urlopen("http://baike.baidu.com/view/146409.htm").read()
start=content.find(r'全体会员国和它们的加入日期如下')
end=content.find(r'按简体中文笔画顺序排列的联合国会员国')
cutcontent=content[start:end]
num=0
count=1

link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", cutcontent)
fileurl=open('test.txt','w')
for url in link_list:
    #字符串包含wiki或/w/index.php则正确url 否则A-Z
    if  url.find('subview')<=0:
        fileurl.write(url+'\n')
        num=num+1
fileurl.close()
print 'URL Successed! ',num,' urls.'

for url in link_list:
    if  url.find('subview')<=0:
        baikeurl='http://baike.baidu.com'+str(url)
        #print baikeurl
        country=urllib2.urlopen(baikeurl).read()
        name=str(count)+'country.html'
        open(r'country/'+name,'w+').write(country)
        count=count+1
        print 'Crawler Successed',count,'\n'