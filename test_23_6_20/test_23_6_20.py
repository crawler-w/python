# 面向对象的使用：数据分析
# 某公司有两份数据文件，现需对其进行分析处理，计算其每日销售额，并以柱状图的形式进行展示

# 总体思路：要采用面向对象的编程思想
# 1、数据存储 ---- 设计一个类，记录读取的数据
# 2、读取数据 ---- 设计一个类（父类是声明（设计），子类是具体实现，text文件和json文件，所有应该有两个子类，此处用到多态），可以从文件中读取数据
# 3、数据计算 ---- 将每个月的销售额加和
# 4、数据可视化显示 ---- 将计算结果显示成统计图



from file_define import fileReader, textFileReader, jsonFileReader
from data_record import Record
from pyecharts.charts import Bar # 通过Bar可以创建柱状图对象
from pyecharts.options import * # 导入选项，柱状图的选项
from pyecharts.globals import ThemeType # 主题

def readData(fileReader: fileReader) -> list[Record]: # 传入子类对象读取数据
    return fileReader.readData() # 将读取的数据返回

# 从文件中读取数据
tf = textFileReader('D:/github-python/test_23_6_20/2011年1月销售数据.txt') # 创建对象
jf = jsonFileReader('D:/github-python/test_23_6_20/2011年2月销售数据JSON.txt') # 创建对象
dl1: list[Record] = readData(tf)
dl2: list[Record] = readData(jf)
dl = dl1 + dl2 # 两个列表相加

# 计算数据：将每一天的数据的销售额加和
# 思路：采用字典进行统计，如下：让日期当键，让销售总额当值
# dict = {'2001-01-01': 1000, '2001-01-02':2000......}
dataDict = {}
for record in dl: # 从列表中拿出来每一套记录
    if record.date in dataDict.keys(): # 如果当前字典中有该日期，则累加，否则加入
        dataDict[record.date] += record.money # 进行累加
    else:
        dataDict[record.date] = record.money # 加入新的键值：对于字典而言：如果没有存在次键值对，赋值语句就是加入新的，如果存在，则就是赋值

#print(dataDict) # 打印统计的数据

# 数据的可视化显示
bar = Bar() # 创建柱状图对象

bar.add_xaxis(list(dataDict.keys())) # 添加x轴的数据
bar.add_yaxis('销售额', list(dataDict.values()), label_opts = LabelOpts(is_show = False)) # 添加y轴数据
bar.set_global_opts(
    title_opts = TitleOpts(title = '每日销售额')
)
bar.render('每日销售额柱状图.html')





