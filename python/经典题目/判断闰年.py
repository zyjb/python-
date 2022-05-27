'''
闰年，能被四整除的年份
非整百年：能被4整除的为闰年。
整百年：能被400整除的是闰年。
'''
import random
a = input("输入年份：")
if int(a) > 0 and int(a) % 4 == 0 and int(a) % 400 == 0:
    print('Ture')
else:
    print('False')

