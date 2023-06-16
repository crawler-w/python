#实现一个猜数字游戏，数字范围是1~100
import random
num = random.randint(1, 100) # 产生1~100之间的随机数
print("[猜数字游戏开始！]")
count = 0 # 记录猜测了多少次
while True:
    n = int(input("请输入你要猜测的数字："))
    count += 1
    if n == num:
        print(f"[恭喜你猜对了，游戏结束，你总共猜了{count}次]")
        break
    elif n < num:
        print("你猜小了")
    elif n > num:
        print("你猜大了")
