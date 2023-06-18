# 自定义模块：文件处理相关功能

# 接收传入文件的路径，打开文件的全部内容，如：文件不存在则捕获异常，输出提示信息，通过finally关闭文件
def printFileInfo(fileName):
    try: # 捕获异常
        f = open(fileName, 'r', encoding = 'utf-8')
        for line in f: # 从文件对象中获取每一行
            print(line, end = '') # 打印每一行，并且去掉后面的自动换行
    except FileNotFoundError: # 处理异常
        print('没有找到文件，请检查问价路径和文件！')
    finally:
        f.close() # 关闭文件

# 接收文件路径以及传入的数据，将数据追加写入到文件中
def appendToFile(fileName, data):
    try:
        f = open(fileName, 'a', encoding = 'utf-8')
        f.write(data) # write参数必须是字符串
    except FileNotFoundError:
        print("没有找到文件，请检查文件路径和文件！")
    finally:
        f.close()


# 追加文件代码测试
if __name__ == '__main__':
    appendToFile('d:/gitee-python/custom toolkit practice/word.txt', '\n这是一首来自person的诗')

# 读取文件代码测试
if __name__ == '__main__':
    printFileInfo('d:/gitee-python/custom toolkit practice/word.txt')