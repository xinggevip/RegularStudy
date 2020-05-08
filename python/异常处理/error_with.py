try:
    with open('data.txt','w') as f:
        f.write('写入内容')
        for each_line in f:
            print(each_lin)
except OSError as reason:
    print('出错了：' + str(reason))
