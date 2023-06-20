'''
声明一些和存储数据相关的类
'''

class Record:
    def __init__(self, date: str, orderId: str, money: int, province: str):  # 构造函数
        self.date = date              # 订单日期
        self.orderId = orderId        # 订单id
        self.money = money            # 订单金额
        self.province = province      # 销售省份

    def __str__(self):
        '''
        没有__str__()魔术方法，通过print打印自定义Record类型的时候，打印的是地址，
        有了它，可以将将print输出的内容转换成字符串
        '''
        return f'日期：{self.date}, 订单id：{self.orderId}, 订单金额：{self.money}, 销售省份：{self.province}'