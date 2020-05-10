# -*- coding:utf-8 -*-
# @Time: 2020/5/10 15:19
# @Author: xinggevip
# @Email: 1511844263@qq.com
# @File: learn01.py

from lxml import etree

# learn01 自定义字符串解析成html

text = \
"""
<body>
<div class="container">
    <div id="first">
        <div class="one">都市</div>
        <div class="two">德玛西亚</div>
        <div class="two">王牌对王牌</div>
        <a>
            <div class="spe">特殊位置</div>
        </a>
    </div>
    <div id="second">
        <div class="three">水电费</div>
        <div class="three">说的话房间不开封</div>
        <div class="four">三顿饭黑客技术</div>
    </div>
    <div id="third">
        <div class="three">水电费</div>
        <div class="three">说的话房间开封</div>
    </div>
</div>
</body>
"""
# 解析成html
html = etree.HTML(text)
result = etree.tostring(html,encoding='utf8').decode('utf8')
print(result)


