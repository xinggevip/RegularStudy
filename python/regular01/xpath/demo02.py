# -*- coding:utf-8 -*-
# @Time: 2020/5/10 20:53
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: demo02.py

import requests
from lxml import etree

response = requests.get('https://www.baidu.com')

response.encoding = 'utf-8'

selector = etree.HTML(response.text)
news_text = selector.xpath('//*[@id="u1"]/a/text()')
news_url = selector.xpath('//*[@id="u1"]/a/@href')
links = []

length = len(news_text)
for i in range(length):
    link = {
        "new_text":news_text[i],
        "new_url":news_url[i]
    }
    links.append(link)
for val in links:
    print(val)

print('------第二种写法----------')

list = []
for text,url in zip(news_text,news_url):
    item = {
        "title":text,
        "url":url
    }
    list.append(item)
for item in list:
    print(item)