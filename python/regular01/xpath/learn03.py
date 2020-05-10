# -*- coding:utf-8 -*-
# @Time: 2020/5/10 15:54
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: learn03.py

from lxml import etree

# learn03使用自定义的parser，解决导入html解析异常
# TODO 还是报错了，不知道什么原因

parser = etree.HTMLParser(encoding='utf8')

html = etree.parse(r'D:\知识库\文本\编程\xpath\xpath(2)\实例文件\baidu.html',parser=parser)
result = etree.tostring(html,encoding='utf8').decode('utf8')
print(result)