import time


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleeptime(0, 0, 5)
while 1 == 1:
    time.sleep(second)
    print('do action')
# 这是隔5秒执行一次
