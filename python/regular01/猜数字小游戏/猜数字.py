print("猜数字游戏")

guess = int(input("请输入有一个数字："))
num = 0
while num < 3:
    num = num+1
    guess = int(input("猜错了，请重新输入一个数字："))
    if guess == 8:
        print("恭喜你猜对了")
    else:
        if guess > 8:
            print("大了大了")
        else:
            print("小了小了")
print("游戏结束")
