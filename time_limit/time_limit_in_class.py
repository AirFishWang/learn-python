# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     time_limit
   Description :
   Author :        wangchun
   date：          2019/5/24
-------------------------------------------------
   Change Activity:
                   2019/5/24
-------------------------------------------------
"""
import signal
import time

def debug(func):
    def _deco(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        self = args[0]
        server_url = "http://%s:%s" % (self.host, self.port)
        print(server_url)
        return server_url
    return _deco


class Command(object):
    def __init__(self, host, port=10000):
        self.host = host
        self.port = port

    @debug
    def create(self, data):
        pass




def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                print('start alarm signal.')
                r = func(*args, **kwargs)
                print('close alarm signal.')
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback(args[1])

        return to_do

    return wrap


def after_timeout(t):  # 超时后的处理函数
    print("Time out {}!".format(t))


class CommandV2(object):
    def __init__(self):
        pass

    @set_timeout(3, after_timeout)
    def connect(self, t):  # 要执行的函数
        time.sleep(t)    # 函数执行时间，写大于2的值，可测试超时
        print('Finished without timeout.')


if __name__ == '__main__':
    cmd = Command("1", 1)
    cmd.create({})

    cmd = CommandV2()
    cmd.connect(4)

