import random

number = random.randint(1, 100)
guess = -1

print("我想了一个1到100之间的数字。")

while guess != number:
    guess = int(input("猜一猜这个数字是多少："))

    if guess < number:
        print("太小了！")
    elif guess > number:
        print("太大了！")

print("恭喜你，猜对了！")
