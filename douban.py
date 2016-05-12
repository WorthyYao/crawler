#coding=utf-8
from pymongo import MongoClient
import urllib2
import re
from  lxml import etree
import dic



conn=MongoClient('localhost',27017)
db = conn.douban

class DBDS:
    def __init__(self):
        self.baseurl="https://book.douban.com/tag/"
        self.pageIndex=0

    def getPage(self,baseurl,pageIndex):
        url=baseurl+str(pageIndex)
        return url


    def list_html_crawl(self,coll,urls):

        content=urllib2.urlopen(urls).read()
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
                try:
                    name=book_name[0].text.encode('utf-8')
                    author=book_author[0].text.encode('utf-8')
                    score=book_score[0].text.encode('utf-8')
                    nums=book_nums[0].text.encode('utf-8')
                    book={"name":name, "author":author, "score":score, "nums":nums}
                    coll.insert(book)
                except:
                    pass

    def start(self):
        base_tag_html=urllib2.urlopen("https://book.douban.com/tag").read()

        re_tag=r'<a href="/tag/(.*?)"'
        base_tag=re.findall(re_tag,base_tag_html,re.S|re.M)

        for tag in base_tag:
            en_tag=dic.d[tag]
            coll=db[en_tag]
            self.pageIndex=0
            baseurl=self.baseurl+tag+"?start="
            while(self.pageIndex<=0):
                url=self.getPage(baseurl,self.pageIndex)
                self.pageIndex+=20
                print "*******开始下载"+url+"下的20本书************\n"
                self.list_html_crawl(coll,url)



spider=DBDS()
spider.start()