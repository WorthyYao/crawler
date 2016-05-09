#学习了xpath选取的基本操作

#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import re
from lxml import etree
info=open('infobox.txt','w')

content_html=urllib2.urlopen("https://book.douban.com/subject/26761569/").read()
html = etree.HTML(content_html)
book_name=html.xpath('//*[@id="wrapper"]/h1/span')
book_author=html.xpath('//*[@id="info"]/span[1]/a')
book_score=html.xpath('//*[@id="interest_sectl"]/div/div[2]/strong')
book_nums=html.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span')



print book_name[0].text
print book_author[0].text
print book_score[0].text
print book_nums[0].text
name=book_name[0].text.encode('utf-8')
author=book_author[0].text.encode('utf-8')
score=book_score[0].text.encode('utf-8')
nums=book_nums[0].text.encode('utf-8')

info.write(name)
info.write(author)
info.write(score)
info.write(nums)

