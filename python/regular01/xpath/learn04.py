# -*- coding:utf-8 -*-
# @Time: 2020/5/10 16:22
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: learn04.py

from lxml import etree

position = \
    """
<ul class="ullist" padding="1" spacing="1">
    <li>
        <div id="top">
            <span class="position" width="350">职位名称</span>
            <span>职位类别</span>
            <span>人数</span>
            <span>地点</span>
            <span>发布时间</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
            </span>
            <span>技术类</span>
            <span>4</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
    </li>
</ul>
"""


# 判断变量类型的函数
def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "list"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    return type


# 返回变量类型
def getType(variate):
    arr = {"int": "整数", "float": "浮点", "str": "字符串", "list": "列表", "tuple": "元组", "dict": "字典", "set": "集合"}
    vartype = typeof(variate)
    if not (vartype in arr):
        return "未知类型"
    return arr[vartype]


html = etree.HTML(position)

# 1.获取所有的div
divs = html.xpath('//div')
for div in divs:
    d = etree.tostring(div, encoding='utf8').decode()
    print(d)
    print('*' * 50)

# 2.获取指定的div
print('----------------divOne--------------------')
divOne = html.xpath('//div[2]')[0]
print("{0}是{1}".format(divOne,getType(divOne)))
divOneRes = etree.tostring(divOne, encoding='utf8').decode()
print(divOneRes)


print('----------------divsTwo--------------------')
# 3.根据属性获取div
divsTwo = html.xpath('//div[@id="even"]')
for div in divsTwo:
    d = etree.tostring(div, encoding='utf8').decode()
    print(d)
    print('*' * 50)

print('----------------ids--------------------')
# 4.获取标签的属性值
ids = html.xpath('//div/@id')
print(ids)


print('----------------divsThree--------------------')
# 5.获取除了第一个div外其他div中的a标签的href属性值
divsThree = html.xpath('//div')[1:]
works = []
for div in divsThree:
    work = {}
    # 获取href值
    href = div.xpath('.//a/@href')[0]
    # print(href)
    # 获取工作名称
    position = div.xpath('.//a/text()')[0]
    # print(position)
    # 获取工作类型
    workType = div.xpath('./span[2]/text()')[0]
    # print(workType)
    # 获取工作时间
    workTime = div.xpath('./span[5]/text()')[0]
    # print(workTime)
    # 获取工作地点
    workLocal = div.xpath('./span[4]/text()')[0]
    # print(workLocal)
    # 获取人数
    num = div.xpath('./span[3]/text()')[0]
    # print(num)
    work = {
        "href":href,
        "position":position,
        "workType":workType,
        "workTime":workTime,
        "workLocal":workLocal,
        "num":num
    }
    # print(work)
    works.append(work)


for work in works:
    print(work)
