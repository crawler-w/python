# 自定义模块：字符串处理相关功能

# 反转字符串：从后往前遍历字符串，然后依次和空串进行拼接
def strReverse(s): # 由于字符串是不可以修改的，所有反转后的字符串是一个新串
    mystr = "" # 定义一个空串
    mylen = len(s) # 求字符串的长度
    i = -1
    while i >= -mylen: # 从后往前遍历所有字符
        mystr += s[i] # 字符串拼接
        i -= 1 # 更新i
    return mystr

# 按照下标x和y对字符串进行切片：先找到x到y区间的字符串，然后将整个字符串替换成该字符串
def subStr(s, x, y):
    tmpStr = s[x : y + 1] # 对字符串进行切片，注意：左闭右开区间
    s = s.replace(s, tmpStr) # 注意replace函数有返回值
    return s

# 反转字符串测试代码
if __name__ == '__main__':
    print(strReverse("hello bit!"))

# 字符串切片测试代码
if __name__ == '__main__':
    print(subStr("hello bit!", 6, 8))
