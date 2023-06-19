# # 程序员鼓励师
# # pynput库，监听键盘
# # playsound库，播放音乐
# # 需要准备音频
#
# from pynput import keyboard  # 从pynput中导入keyboard对象
# from playsound import playsound
# import random
# from threading import Thread # 线程模块
#
# soundList = ['1.wav', '2.mp3'] # 创建一个音频列表
# count = 0
# def onRelease(key):
#     """
#     这个函数是释放键盘按键的时候会被listener自动调用，这就叫做回调函数
#     :param key:用户按下了哪个键
#     :return:
#     """
#     # print(key) # 打印一下按下了哪个键
#     global count # 说明他是一个全局变量
#     count += 1
#     if count % 10 == 0: # 每按键按10次播放一次音乐
#         # 产生一个随机数，randint()产生的范围是左闭右闭，而for循环中用到的ranger是左闭右开
#         i = random.randint(0, len(soundList) - 1)
#         # playsound(soundList[i])
#         # # 我们发现当音乐长度很长的时候，我们敲击键盘次数满足播放音乐的时候，播放音乐如果没有结束，会导致键盘卡顿
#         # # 此时我们应该采用线程解决
#         t = Thread(target=playsound, args=(soundList[i], )) # 创建一个线程，并给其安排任务
#         t.start() # 启动线程
#         # 线程就相当于，你有垃圾要倒，有快递要取，但是你只能先做完一样再去完成另一个，
#         # 而有了线程之后，就相当于你叫上你的好兄弟，你去拿快递，他去帮你倒垃圾
#
# # 创建listener好了之后，listener就可以监听键盘，on_release是一个函数指针，这里是回调函数
# # onRelease是一个自定义函数，你可以定义释放键盘按键的时候做什么操作
# listener = keyboard.Listener(on_release=onRelease) # 这里只是创建Listener并安排任务
# listener.start() # 启动监听
# listener.join() # 为了防止退出，一直等待用户输入