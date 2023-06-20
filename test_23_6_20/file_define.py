'''
声明一些和文件相关的类
'''
import json

from data_record import Record
class fileReader: # 读取文件类
    def readData(self) -> list[Record]:
        '将读取到的每一条数据转换为Record对象，最后通过列表返回'
        pass


class textFileReader(fileReader): # 文本文件读取类
    def __init__(self, path: str): # 构造函数，获取文件路径
        self.path = path

    def readData(self) -> list[Record]: # 复写父类函数（实现虚函数）
        recordList = []
        with open(self.path, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip() # 去掉尾部换行符
                dataList = line.split(',') # 根据逗号分割字符串
                record = Record(dataList[0], dataList[1], int(dataList[2]), dataList[3]) # 创建一个Record对象，记录数据
                recordList.append(record) # 将Record对象加入列表
        return recordList # 返回列表

class jsonFileReader(fileReader): # json文件读取类
    def __init__(self, path: str):  # 构造函数，获取文件路径
        self.path = path

    def readData(self) -> list[Record]:  # 复写父类函数（实现虚函数）
        recordList = []
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                dataDict = json.loads(line) # 将json格式的字符串转换成字典类型
                record = Record(dataDict['date'], dataDict['order_id'], dataDict['money'], dataDict['province'])
                recordList.append(record)
        return recordList  # 返回列表


if __name__ == '__main__': # 测试代码
    # # 文本文件测试
    # tf = textFileReader('D:/github-python/test_23_6_20/2011年1月销售数据.txt')
    # dataList1 = tf.readData()
    # for dl in dataList1:
    #     print(dl)

    # json文件测试
    jf = jsonFileReader('D:/github-python/test_23_6_20/2011年2月销售数据JSON.txt')
    dataList2 = jf.readData()
    for dl in dataList2:
        print(dl)


