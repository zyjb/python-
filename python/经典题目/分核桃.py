'''小张是软件项目经理，他带领 3 个开发组。工期紧，今天都在加班呢。为鼓舞士气，小张打算给每个组发一袋核桃
（据传言能补脑）。他的要求是：
各组的核桃数量必须相同
各组内必须能平分核桃（当然是不能打碎的）
尽量提供满足 1,2 条件的最小数量（节约闹革命嘛）
输入格式
输入包含三个正整数 a, b, c，表示每个组正在加班的人数，用空格分开（a,b,c<30）
输出格式
输出一个正整数，表示每袋核桃的数量。
样例输入 1
2 4 5
样例输出 1
20
样例输入 2
3 1
样例输出 2
3
'''
a = input("a组加班人数：")
b = input("b组加班人数：")
c = input("c组加班人数：")
common_multiple = 0
if common_multiple % int(a) == 0 and common_multiple % int(b) == 0 and common_multiple % int(c) == 0:
    print(min.common_multiple)



