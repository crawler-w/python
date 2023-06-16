# # while循环求1~100的和
# i = 1
# thesum = 0
# while i <= 100:
#     thesum += i
#     i += 1
# print(f"sum = {thesum}")
#
#
#
# # while打印n*n乘法表
# n = int(input("请输入一个正整数："))
# i = 1
# while i <= n: # 打印n行
#     j = 1
#     while j <= i: # 打印一行
#         print(f"{i} * {j} = {i * j}\t", end = '') # 在print语句中加上end = ''可以不换行
#         j += 1
#     print() # print空语句就输出个换行
#     i += 1

# # pop是通过下标删除一个元素并且返回该元素，列表（可以输入下标）、元组和字符串（不可以删除）、集合（随意删除一个元素）、字典（用键充当下标）
# mylist = ["hello", "world", "bit"]
# element = mylist.pop(1)
# print(f"element = {element}")
# print(f"mylist = {mylist}")


# # 字典的一些相关操作
# a = {
#     'name': '王海楼',
#     'age': 22,
#     'gender': '男',
#     'score': 99.5
# }
# # 获取字典内的内容
# keys = a.keys() # 获取所有的键
# print(f"keys = {keys}")
# values = a.values() # 获取所有的值
# print(f"values = {values}")
# items = a.items() # 获取所有的键值
# print(f"items = {items}")
#
# # 遍历字典
# print("第一种")
# for key in a: # 通过for获取到键值来遍历字典
#     print(key, a[key])
#
# print("第二种")
# for key in keys: # 通过在所有的键keys中拿到每一个键来遍历,显然这种方法没有上面那种方法方便，因为要提前获取keys
#     print(key, a[key])
#
# print("第三种")
# mylist = []
# for key, value in items: # 通过在所有的键值items中，获得每一个键和值
#     print(key, value)
# # 第三种items里面是一个列表，列表中的每个元素是元组，如：[('name','王海楼'), ('age', 22), ('男', 99.5)]
# # 如果上面key或者value不写，则获取到的直接就是元组，也就是说key或者item是元组类型，因为从迭代容器中拿到的是每一个元素

# # 字典的练习：升职加薪
# department = {
#     '王力鸿': {
#         '部门': '科技部',
#         '工资': 3000,
#         '级别': 1
#     }, '周杰轮': {
#         '部门': '市场部',
#         '工资': 5000,
#         '级别': 2
#     }, '林俊节': {
#         '部门': '市场部',
#         '工资': 7000,
#         '级别': 2
#     }, '张学油': {
#         '部门': '科技部',
#         '工资': 4000,
#         '级别': 1
#     }, '刘德滑': {
#         '部门': '市场部',
#         '工资': 6000,
#         '级别': 2
#     }
# }
#
# print("[全体员工当前信息如下：]")
# print("加薪前：")
# for key in department:
#     print(f"key = {key} : {department[key]}")
#
# # 对所有级别为1级的员工，级别上升1级，薪水增加1000元
# for key in department:
#     if department[key]['级别'] == 1:
#         department[key]['工资'] += 1000
#
# print("加薪后：")
# for key in department:
#     print(f"key = {key} : {department[key]}")