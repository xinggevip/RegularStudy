try:
    
    f = open('文件.txt','w')
    print(f.write('我是文本内容'))
    sum = 1 + '1'
except (OSError,TypeError):
    print('出错了T_T')
finally:
    f.close()
    
