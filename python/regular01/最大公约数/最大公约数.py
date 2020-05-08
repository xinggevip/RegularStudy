def gys(num):
    count = num // 2
    while count > 1:
        if num % 2 == 0:
            print('%d最大的约数为%d' % (num,count))
            break
        count -= 1
    else:
        print('%d是一个素数' % num)
num = int(input('请输入一个数'))
gys(num)
