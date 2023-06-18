# 这是一个自定义模块

def add(x, y): # 两个数相加
    print(x + y)

def sub(x, y): # 两个数相减
    print(x - y)

# 下面是编程人员为了测试上面写的函数而写的测试代码
# __name__是每个python文件中的内置变量，当执行当前文件的时候，__name__就会自动被修改为__main__
# 而当调用该模块的时候__name__就不是__main__，经过测试发现是该模块名，此时下面的代码不会执行
if __name__ == '__main__':
    add(1, 2)
    sub(1, 2)
print(f"name = {__name__}")