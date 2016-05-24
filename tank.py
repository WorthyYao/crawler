#coding=utf-8
import urllib2
import re
baseurlpart="http://news.baidu.com/ns?word=%s&pn="

company_txt="a.txt"

f=open(company_txt,'r')
company_names=f.readlines()
f.close()
for name in company_names:
    name=name.strip('\n')
    print name
    pagenum=0
    f=open('url/%s.txt' %name,'w')
    base_url=baseurlpart %name+str(pagenum)
    print base_url
    base_url_html=urllib2.urlopen(base_url).read()


    re_href=r'<h3 class="c-title">.*?<a href="(.*?)"'



    if "抱歉，没有找到" in base_url_html:
        print "Not Found This Company"
    else:
        content=re.findall(re_href,base_url_html,re.S|re.M)
        for detail_url in content:
            f.write(detail_url+'\n')

        while "下一页" in base_url_html:
            pagenum+=10
            base_url=baseurlpart %name+str(pagenum)
            base_url_html=urllib2.urlopen(base_url).read()
            content=re.findall(re_href,base_url_html,re.S|re.M)
            for detail_url in content:
                f.write(detail_url+'\n')
    f.close()
# num="中国"
# f=open('url/%s.txt' %num,'w')

# f.close()
#
# for i in range(0,150):
# 	fp = file( 'url/%d.txt' % i, 'w')
# 	fp.write( '#%d' % i )
# 	fp.close()
