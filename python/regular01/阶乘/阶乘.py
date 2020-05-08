def jc(x):
    if x == 1:
        return 1
    else:
        return x * jc(x-1)
print(jc(5))

s = 1
for i in range(1,6):
    s = s * i
    print(s)
print(s)
