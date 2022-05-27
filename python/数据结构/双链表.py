
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None
# 实现增删改查

class Dlist(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 1

    def add_1(self,value):  # 头插入
        if self.head is None:
            node = Node(value)
            self.last = node
            self.head = node
            return 0
        node = Node(value)
        node.next = self.head
        self.head.pre = node
        self.head = node
        self.length += 1

    def add_2(self,value):
        if self.last is None:  # 链表为空时
            node = Node(value)
            self.last = node
            self.head = node
            return 0
        node = Node(value)
        node.pre = self.last
        self.last.next = node
        self.last = node
        self.length += 1

    def add_3(self,index,value):
        if index != 1 and self.last is None:
            print('空链表只能在第一位插入')
            return 0
        if index == 1 and self.last is not None:
            node = Node(value)
            self.last = node
            self.head = node
            return 0

        if index >= self.length:
            print('list index out of range')
            return  0

        node = Node(value)
        temp = self.head
        cur = 1
        while cur != index-1:
            temp = temp.next
            cur += 1
        node.next = temp.next
        node.pre = temp
        temp.next = node
        node.next.pre = node
        self.length += 1

    def delete(self,index):
        if self.last is None:
            print('空链表不能删除元素！')
            return 0
        if index>self.length:
            print('list index out of range')
            return 0
        if index == self.length == 1:
            self.last = self.head = None
            self.length -= 1
            return 0
        if index == 1:
            self.head.next.pre = None
            self.head = self.head.next
            self.length -= 1
            return 0
        if index == self.length:
            self.last.pre.next = None
            self.last = self.last.pre
            self.length -= 1
            return 0
        cur = 1
        temp = self.head
        while cur != index-1:
            cur = cur+1
            temp = temp.next
        temp.next.next.pre = temp
        temp.next = temp.next.next
        self.length -= 1

    def change(self,index,value):
        if self.head is None or index>self.length:
            print('list index out of range')
            return 0
        temp = self.head
        cur = 1
        while cur != index:
            cur += 1
            temp = temp.next
        temp.value = value

    def select(self,index):
        if self.head == None or index > self.length:
            print('none')
            return  0
        cur = 1
        temp = self.head
        while cur != index:
            cur+=1
            temp = temp.next
        print('第{}个元素为：'.format(index),temp.value)

    def get_data(self):
        temp = self.head
        if temp is None:
            print('空链表没有元素！！')

        while temp is not None:
            print(temp.value)
            temp = temp.next


d = Dlist()
d.add_1('a')
d.add_1('b')
d.add_1('c')
d.add_2('a')
d.add_2('b')
d.add_2('c')

d.add_3(5,'w')
# d.delete(6)
d.change(6,7)
d.select(5)
d.get_data()

print('长度:',d.length)