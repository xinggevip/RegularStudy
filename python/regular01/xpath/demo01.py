# -*- coding:utf-8 -*-
# @Time: 2020/5/10 18:51
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: demo01.py

# 抓取百度网页

# 1.导入必要的库和模块
import requests
from lxml import etree

# 2.定义网页和请求头
url = "https://www.baidu.com/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
# 3.获取网页html页面（定义编码和转码的问题）
response = requests.get(url,headers)
response.encoding='utf8'
# 4.etree解析
html = etree.HTML(response.text)
# 5.观察源码，查看标签特征

# 6.编写xpath语法，获取表标签内容（文本信息末尾添加/text()
# //*[@id="s-top-left"]/a[1]
avalues = html.xpath('//input[@id="su"]/text()')
print(avalues)
# 7.存储数据（zip函数双循环）