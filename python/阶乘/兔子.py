def tunum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        n = tunum(n - 1) + tunum(n - 2)
        return n
num1 = int(input('请输入月份：'))
nn = tunum(num1)
print('%d 月后有 %d 只兔子'%(num1,nn))
