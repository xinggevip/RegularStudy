try:
    print(int('123'))
except ValueError as reson:
    print('出错了：' + str(reson))
else:
    print('没有任何错误')
