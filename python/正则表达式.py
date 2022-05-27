# # s = '1a2b'   # ->  12 ab
# import random
# s = ['12aa22aa33cc']  # -> 122233   aaaacc
# def random_n():
#     return random.randrange(0,10)
# def random_a():
#     return random.randrange(97,123)
# def random_A():
#     return random.randrange(65,91)
# def random_l():
#     return random.randrange(1,999)
# def random_x():
#     return random.randrange(0,4)
# def return_p():
#     return '['
# s = ''
# for _ in range(random_l()):
#     x = random_x()
#     if x == 0:
#         s = s+str(random_n())
#     if x == 1:
#         s = s+chr(random_a())
#     if x == 2:
#         s = s+chr(random_A())
#     if x == 3:
#         s = s+return_p()
# # print(s)
# a_n = ''
# for i in s:
#     #print(i)
#     if ord(i)>=48 and ord(i)<=122:
#         a_n = a_n+i
#         print(a_n)

# 非贪婪模式  叫做深度优先搜索
# 贪婪模式 叫做 广度优先搜索
import re
s1 = "<a href='http://www.runoob.com/python/python-reg-expressions.html'>这是一个链接</a> <a href='https://wwww.runoob.com/python/python-reg-expressions.html'>这是一个链接</a>"

s2= re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")

ss2 = s2.findall(s1)
print(ss2)
# for i in range(5):
#     print(1)
#     try:
#         print(ss1[0])
#     except Exception as e:
#         raise e


