# -*- coding:utf-8 -*-
# @Time: 2020/5/10 15:42
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: learn02.py

from lxml import etree

# learn02 导入html文件并解析成html

html = etree.parse(r'D:\知识库\文本\编程\xpath\xpath(2)\实例文件\test.html')
result = etree.tostring(html,encoding='utf8').decode('utf8')
print(result)
