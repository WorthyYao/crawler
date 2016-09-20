#coding=utf-8
import urllib2
import re
from pymongo import MongoClient
import time

conn=MongoClient('localhost',27017)
baby_db = conn.baby

coll_baby=baby_db['baby']

browse_base_url="http://baobao.baidu.com/browse?pn="
detail_base_url="http://baobao.baidu.com/question/ajax/replymore?qid="

re_ul=r'<section class="question-list">(.*?)</section>'
re_li=r'<li>(.*?)</li>'
re_href=r'<a href="/question/(.*?).html"'
re_num=r'<span class="reply-text">(.*?)回答</span>'

re_answer=r'<p>(.*?)</p>'
re_username=r'<a class="username">(.*?)</a>'
re_date=r'<span class="time">(.*?)</span>'

for i in range(0,1,20):
    browse_url= browse_base_url+str(i)
    try:

        html=urllib2.urlopen(browse_url).read()
        print "parse"+' '+browse_url
        time.sleep(2)
        ul=re.findall(re_ul,html,re.S|re.M)[0]
        lis=re.findall(re_li,ul,re.S|re.M)
        for li in lis:
            href=re.findall(re_href,li,re.S|re.M)[0]
            num=re.findall(re_num,li,re.S|re.M)[0]
            detail_url=detail_base_url+href+'&pn=0&rn='+num

            time.sleep(1)
            try:

                html=urllib2.urlopen(detail_url).read()
                print "process"+' '+detail_url

                solution=[]
                answers=re.findall(re_answer,html,re.S|re.M)
                usernames=re.findall(re_username,html,re.S|re.M)
                dates=re.findall(re_date,html,re.S|re.M)

                for j in range(len(answers)):
                    answer=answers[j]
                    username=usernames[j]
                    date=dates[j]
                    data={"answer":answer,"username":username,"date":date}
                    solution.append(data)

                result={}
                result['solution']=solution

                coll_baby.insert(result)
            except urllib2.HTTPError, e:
                print e.code
            except urllib2.URLError, e:
                print e.reason

    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.reason
