import random

# 生成一个1至100的随机整数
number = random.randint(1, 100)

# 记录猜测次数
count = 0

print("猜数字游戏开始！")

while True:
    # 让用户输入猜测的数字
    guess = input("请输入一个1至100的整数：")
    
    # 将用户输入的字符串转换成整数
    guess = int(guess)
    
    # 猜测次数加1
    count += 1
    
    # 判断猜测的数字是否正确
    if guess == number:
        print("恭喜你，猜对了！你一共猜了%d次。" % count)
        break
    elif guess < number:
        print("猜的数字太小了，请再猜一次。")
    else:
        print("猜的数字太大了，请再猜一次。")
