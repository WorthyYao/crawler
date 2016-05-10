#coding=utf-8

import urllib2
import re
from  lxml import etree
info=open('douban.txt','w')


class DBDS:
    def __init__(self):
        self.baseurl="https://book.douban.com/tag/小说?start=20"
        self.pageIndex=0

    def getPage(self,pageIndex):
        url="https://book.douban.com/tag/小说?start="+str(pageIndex)
        return url


    def list_html_crawl(self,url):

        content=urllib2.urlopen("https://book.douban.com/tag/小说?start=20&type=T").read()
        re_info=r'<h2 class.*?>.*?</h2>'
        content=re.findall(re_info,content,re.S|re.M)
        for con in content:
            re_href=r'href="(.*?)"'

            urldetail=re.findall(re_href,con,re.S)
            for url in urldetail:
                print url
                book_html=urllib2.urlopen(url).read()
                html = etree.HTML(book_html)
                book_name=html.xpath('//*[@id="wrapper"]/h1/span')
                book_author=html.xpath('//*[@id="info"]/span[1]/a')
                book_score=html.xpath('//*[@id="interest_sectl"]/div/div[2]/strong')
                book_nums=html.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span')
                name=book_name[0].text.encode('utf-8')
                author=book_author[0].text.encode('utf-8')
                score=book_score[0].text.encode('utf-8')
                nums=book_nums[0].text.encode('utf-8')
                info.write(name+' ')
                info.write(author)
                info.write(score)
                info.write(nums+'\n')

    def start(self):
        while(self.pageIndex<=20):
            url=self.getPage(self.pageIndex)
            self.list_html_crawl(url)
            self.pageIndex+=20



spider=DBDS()
spider.start()