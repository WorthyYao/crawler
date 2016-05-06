//抓取百度百科的信息盒中的属性值，这次爬取的是所有联合国会员国的属性信息


# coding=utf-8

import urllib2
import re

info=open('infobox.txt','w')
content = urllib2.urlopen("http://baike.baidu.com/view/146409.htm").read()
start=content.find(r'全体会员国和它们的加入日期如下')
end=content.find(r'按简体中文笔画顺序排列的联合国会员国')
cutcontent=content[start:end]
num=0
count=1
# link_list中存储了所有的国家的url
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

        start=country.find(r'<div class="basic-info cmn-clearfix"') #起点记录查询位置
        end=country.find(r'<div class="lemmaWgt-lemmaCatalog">')    #减去1个空格
        # 截取infobox，得到了一个具体国家的信息盒
        infobox=country[start:end]
        open(r'country/'+name,'w+').write(infobox)
        print 'Crawler Successed',count,'\n'
        count=count+1


        res=r'<dt.*?</dd>'
        infotable=re.findall(res,infobox,re.S|re.M)
        for line in infotable:
            line= unicode(line,'utf-8')
            # 得到的是属性
            res_name=r'<dt.*?>(.*?)</dt>'
            m_name=re.findall(res_name,line,re.S|re.M)
            for mm in m_name:
                mm_nbsp=r'&nbsp;'
                mm=re.sub(mm_nbsp,"",mm)

                mm= mm.encode('utf-8')
                # print mm
                info.write(mm+' ')
            # print line
            # 得到的是属性值
            res_value=r'<dd.*?>(.*?)</dd>'
            n_value=re.findall(res_value,line,re.S|re.M)
            # print n_value
            for nn in n_value:
                if "href" in nn:
                    res_href=r'<a.*?>(.*?)</a>'
                    nn=re.findall(res_href,nn,re.S|re.M)
                    for value in nn:
                        value=value.encode('utf-8')
                        info.write(value+' ')
                    info.write('\n')
                else:
                    re_n=r'\n'
                    nn=re.sub(re_n,'',nn,re.S|re.M)
                    nn=nn.encode('utf-8')
                    info.write(nn)
                    info.write('\n')



