import random

students = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank']  # 学生名单

def random_pick():
    random_student = random.choice(students)
    return random_student

def main():
    while True:
        input("按回车键进行随机点名：")
        random_student = random_pick()
        print("被点到的学生是：", random_student)

if __name__ == '__main__':
    main()
