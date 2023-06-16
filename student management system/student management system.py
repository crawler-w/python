# 学生管理系统

import sys
import os.path

studentsList = [] # 创建一个学生列表，存放学生信息，每个元素都是字典类型

# 主菜单
def mainMenu():
    print('*******************************************')
    print('*****         《学生管理系统》          *****')
    print('*****           1、新增学生            *****')
    print('*****           2、显示学生            *****')
    print('*****           3、删除学生            *****')
    print('*****           4、查找学生            *****')
    print('*****           0、退出程序            *****')
    print('*******************************************')
    choice = input('请输入你的选择：')
    return choice


# 删除菜单
def deleteMenu():
    print('*******************************************')
    print('*****      《请选择按什么方式删除》       *****')
    print('*****           1、按学号删除           *****')
    print('*****           2、按姓名删除           *****')
    print('*******************************************')
    choice = input('请输入你的选择：')
    return choice

# 查找菜单
def findMenu():
    print('*******************************************')
    print('*****       《请选择按什么方式查找》      *****')
    print('*****           1、按学号查找           *****')
    print('*****           2、按姓名查找           *****')
    print('*****           3、按性别查找           *****')
    print('*****           4、按班级查找           *****')
    print('*******************************************')
    choice = input('请输入你的选择：')
    return choice


# 新增学生
def insert():
    # 先将学生先添加到studentsList变量当中，当程序结束的时候，再将数据保存到文件当中
    # 注意：input的返回值是字符串类型
    print('[新增学生] 开始！')
    n = int(input('请输入你要新增几个学生的信息：'))
    for i in range(0, n): # 循环的是0，1，2，3，...，n-1
        print(f'[正在新增第{i+1}个学生的信息:]')
        while True: # 这里做一个检查，每个学生的学号必须是唯一的
            flagStudentId = 0  # 标记学生学号是否重复，0表示没有重复，1表示重复
            studentId = input('请输入学生学号：')
            for s in studentsList:
                if s['studentId'] == studentId:
                    flagStudentId = 1 # 有重复学号，修改标记
            if flagStudentId == 1:
                print('此学号已存在，请重新输入！')
            else:
                break # 跳出循环
        name = input('请输入学生姓名：')
        while True: # 检查性别是否输出正确
            gender = input('请输入学生性别：')
            if gender not in ('男', '女'):
                print('性别输入错误，请重新输入！')
            else:
                break
        classId = input('请输入学生班级：')
        # 将上面数据放到字典当中，方便管理
        student = {
            'studentId': studentId,
            'name': name,
            'gender': gender,
            'classId': classId
        }
        studentsList.append(student)  # 将学生信息添加到studentsList中
        print(f'第{i+1}个学生的信息新增完毕！')

    print('[新增学生] 结束!')


# 显示学生（显示所有学生信息）
def show():
    print('[显示学生] 开始！')
    print('学号\t\t 姓名\t\t 性别\t\t 班级')
    for s in studentsList: # 循环打印学生信息
        print(f"{s['studentId']}\t\t {s['name']}\t\t {s['gender']}\t\t {s['classId']}")
    print(f'[显示学生] 结束, 总共显示了{len(studentsList)}个学生信息！')


# 按学号或者姓名删除学生，参数为1代表按学号删除，参数为2代表按姓名删除
def deleteByIdOrName(value):
    alist = [] # 创建一个列表，存放满足删除条件的学生
    count = 0 # 计数器
    if value == 1: # 按学号删除
        studentId = input('请输入学生学号:')
        for s in studentsList:  # 查找满足条件的学生
            if studentId == s['studentId']:  # 满足条件
                alist.append(s)  # 将s存到alist中
    else: # 按姓名删除
        name = input('请输入学生姓名：')
        for s in studentsList:  # 查找满足条件的学生
            if name == s['name']:  # 满足条件
                alist.append(s)  # 将s存到alist中

    if len(alist) == 1: # 只有一个满足条件的学生，直接删除
        studentsList.remove(alist[0]) # 用remove，通过值来删除
        print('删除成功！')
    elif len(alist) > 1: # 有多个满足条件的学生，请用户选择
        print('编号\t\t学号\t\t 姓名\t\t 性别\t\t 班级')
        for s in alist: # 先将同名的学生打印
            count += 1
            print(f"{count}\t\t{s['studentId']}\t\t {s['name']}\t\t {s['gender']}\t\t {s['classId']}")
        print(f'总共有{count}个姓名为{name}的学生！')
        while True:
            choice = int(input('请输入你要删除的学生编号：'))
            if 1 <= choice <= count:  # 检验输入是否合法
                studentsList.remove(alist[choice-1])  # 通过值来删除
                break
            else:
                print('输入错误，请重新选择！')
        print('删除成功！')
    else:
        print('没有此学生！')


# 删除学生
def delete():
    while True:
        choice = int(deleteMenu())  # 打印删除相关菜单
        if choice == 1:
            # 按学号删除
            deleteByIdOrName(1) # 参数为1，代表按学号删除
            break
        elif choice == 2:
            # 按姓名删除
            deleteByIdOrName(2) # 参数为2，代表按姓名删除
            break
        else:
            print('输入错误，请重新输入！')

# 打印满足条件的学生信息
def displayInfo(key, info):
    flag = 0 # 用于标记是否有满足条件的学生，0表示没有，1表示有
    count = 0 # 统计满足条件的学生个数
    for s in studentsList:
        if s[key] == info:
            flag = 1 # 修改标记
            count += 1
            print(f"{s['studentId']}\t\t {s['name']}\t\t {s['gender']}\t\t {s['classId']}")
    print(f'[查找学生] 结束，总共有{count}个学生满足查找条件！')

# 按学号、姓名、性别、班级查找
def findSub(value):
    count = 0 # 计数器
    if value == 1:
        # 按学号查找
        studentId = input('请输入学生学号：')
        # 将满足条件的学生信息打印出来,第一个参数是字典的键值，第二个参数是要查找的学生姓名
        displayInfo('studentId', studentId)
    elif value == 2:
        # 按姓名查找
        name = input('请输入学生姓名：')
        displayInfo('name', name)
    elif value == 3:
        # 按性别查找
        while True: # 这里做一个性别检查
            gender = input('请输入学生性别：')
            if gender not in ('男', '女'):
                print('输入错误，请重新输入！')
            else:
                break
        displayInfo('gender', gender)
    elif value == 4:
        # 按班级查找
        classId = input('请输入班级：')
        displayInfo('classId', classId)


# 查找学生
def find():
    while True:
        choice = int(findMenu()) # 打印菜单
        if choice == 1:
            # 按学号查找
            findSub(1)
            break
        elif choice == 2:
            # 按姓名查找
            findSub(2)
            break
        elif choice == 3:
            # 按性别查找
            findSub(3)
            break
        elif choice == 4:
            # 按班级查找
            findSub(4)
            break
        else:
            print('输入错误，请重新输入！')


# 将数据保存到文件当中
def save():
    with open('../test_23_5_12/record.txt', 'w', encoding ='utf8') as f: # 打开文件，f为文件对象，encoding是指定编码格式为utf8
        for s in studentsList:
            # 存到文件中的时候，每个信息间隔一个制表符，方便后面取出
            f.write(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['classId']}\n")

# 将文件中的数据加载到studentsList列表中
def load():
    # 为了防止文件不存在打开失败保存，可以先检查文件是否存在
    if not os.path.exists('../test_23_5_12/record.txt'):
        return
    # 打开文件读取数据
    with open('../test_23_5_12/record.txt', 'r', encoding ='utf8') as f:
        for line in f: # 每次读取一行
            # 针对每一行数据，按水平制表符划分，并存入到列表当中
            # 切分前先将每一行数据后面的换行符去掉，strip()此方法可以将字符串首尾的空白符去掉（空白符包括：换行、制表符、空格等）
            line = line.strip()
            alist = line.split('\t') # 按制表符切分字符串，并存入到列表中
            if len(alist) != 4: # 检测数据是否划分正确
                print('文件内容格式错误！')
                return
            student = {
                'studentId': alist[0],
                'name': alist[1],
                'gender': alist[2],
                'classId': alist[3]
            }
            studentsList.append(student)


# 主函数，程序的整体逻辑
def main():
    load() # 程序每次运行前，先将文件中的数据加载过来
    while True:
        choice = int(mainMenu())  # 打印菜单
        if choice == 1:
            # 新增学生
            insert()
        elif choice == 2:
            # 显示学生
            show()
        elif choice == 3:
            # 删除学生
            delete()
        elif choice == 4:
            # 查找学生
            find()
        elif choice == 0:
            # 退出程序
            save() # 将信息保存到文件当中
            sys.exit()
        else:
            print('输入错误，请重新输入！')


# 调用主函数
main()
