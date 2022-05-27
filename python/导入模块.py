#from print_ import print1
import requests
#
#
response = requests.post('http://www.xs5200.com/')
content = response.content
content = content.decode()
pass
#函数的定义
class student():  #高聚合，低耦合
    #构造函数
    def __init__(self,name,year=18):
        self.number = '20184226004'
        self.year = year
        self.name = name
    def get_name(self):
        return self.year
#函数的调用
s = student(name='赵',year=18)
print(s.get_name())

#inheritance继承






#A,B,C 有五顶帽子，三个白色，两个黑色，会随机分配，每个人只能看到别
# 人头顶的帽子颜色，不能看到自己的，求解，自己头上什么颜色帽子。



# A,B,C,D,E 一百颗宝石，由A开始提出分配策略，如果由一半的人不同意此策略，则A被丢到海里喂鲨鱼。# 递归
#D E
#C D E
#B C D E  100 0 0 0
#A B C D E  97 0 1 1 1

