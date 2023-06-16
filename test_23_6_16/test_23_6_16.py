# 读取文件训练
# 在 word.txt文件中输入下面几行文本：
# itheima itcast python
# itheima python itcast
# beijing shanghai itheima
# shenzhen guangzhou itheima
# wuhan hangzhou itheima
# zhengzhou bigdata itheima
# 通过文件读取操作，读取文件，统计itheima单词出现的次数
# count = 0
# with open("D:/github-python/word.txt", "r", encoding = "utf-8") as f: # 打开文件
#     for line in f: # 每次读取一行
#         count += line.count("itheima") #统计itheima的个数
# print(f"itheima的个数为：{count}")



# # 证明write()函数写文件的时候并没有直接将内容写入到文件当中，而是先写到缓冲区，最后通过flush()函数刷新到文件当中，
# # 或者通过close()关闭文件来写入到文件当中（close()函数内部有flush函数()）
# import time
# f = open("d:/github-python/test.txt", "w", encoding = "utf8")
# for i in range(0, 10): # 循环10次
#     f.write("比特科技\n") # write不会换行
#     time.sleep(2) # 当程序运行的时候,打开test.txt文件查看，并没有内容，单位是秒
# # 并且程序末尾没有写close()函数，当程序结束的时候，test.txt文件中依然是空的，这就说明write是先写到缓冲区中
#
# # 解决方法
# import time
# f = open("d:/github-python/test.txt", "w", encoding = "utf8")
# for i in range(0, 10): # 循环10次
#     f.write("比特科技\n")
#     time.sleep(2)
#     f.flush() # 每写一句都刷新到文件中，但是你要查看的话，要不断的重复打开文件
# # f.flush() 可以写到程序末尾，等全部写道缓冲区后再统一写入
# #f.close() 要么在写close()