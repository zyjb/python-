import _thread
from time import sleep
import numpy as np

items = [2, 4, 10, 3, 1, 7]
# 求平均值
m = np.mean(items)
# 求数字位数
length = len(str(m).split('.')[0])
# 计算等待时间的比例
p = np.power(0.1, length - 1)


# 睡眠排序算法
def sleep_sort(i):
    sleep(i * p)
    print(i)


# 测试：方案1
[_thread.start_new_thread(sleep_sort, (i,)) for i in items]

import threading

# 测试：方案2
[threading.Thread(target=sleep_sort, args=(i,)).start() for i in items]