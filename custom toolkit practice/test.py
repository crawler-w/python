# 自定义工具包测试文件

# 字符串功能函数使用
# 两种导入写法
#from myUtils import * # 前提要在__init__.py文件中添加：__all__ = ['fileUtil', 'strUtil']
from myUtils import fileUtil, strUtil
tmpStr = "你好！破晓而生，踏浪而行~"
print(f"初始字符串：{tmpStr}")
tmpStr = strUtil.subStr(tmpStr, 3, len(tmpStr) - 1) # 将字符串中：你好！去掉
print(f"切片后字符串：{tmpStr}")
tmpStr = strUtil.strReverse(tmpStr) # 逆序字符串
print(f"逆序后字符串：{tmpStr}")
tmpStr = strUtil.strReverse(tmpStr) # 逆序字符串
print(f"再逆序后字符串：{tmpStr}")

# 文件功能函数使用
# 在word.txt文件中追加字符串
fileUtil.appendToFile('d:/gitee-python/custom toolkit practice/word.txt', '\n这是一首来自person的诗')
# 读取文件中的内容
fileUtil.printFileInfo('d:/gitee-python/custom toolkit practice/word.txt')