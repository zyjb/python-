
class Node(object):
    def __init__(self,value):
        self.items = value
        self.next = None




class Slist(object):

    def __init__(self,value=1):
        self.point = None
        self.s_init(value=value)

    def s_init(self,value):
         node = Node(value)
         self.point = node

    # def back_Slist(self,value):
    #     node = Node(value)
    #     while self.point:
    #         self.point= self.point.next
    #     self.point = node
    def add_head(self,value):
        node = Node(value)
        node.next = self.point
        self.point = node

    def back_Slist(self,value):
        node = Node(value)
        temp = self.point
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def inster(self,index,value):
        temp = self.point
        cur = 1


        while cur < index-1:
            cur += 1
            temp = temp.next
        node = Node(value)
        node.next = temp.next
        temp.next = node

    def delete(self,index):
        cur = 1
        temp = self.point
        while cur!=index-1:
            cur = cur+1
            temp = temp.next
        temp.next = temp.next.next



    def get_data(self):
        temp = self.point
        while temp:
            print(temp.items)
            temp = temp.next

    def get_length(self):
        temp = self.point
        len = 0
        while temp:
            len = len + 1
            temp= temp.next
        return len




    def change(self,index,value):
        if index>self.get_length():
            print('list index out of range')
            return 0
        cur = 1
        temp = self.point
        while cur != index:
            cur = cur+1
            temp =temp.next
        temp.items = value

    def select(self,index):
        if index>self.get_length():
            print('list index out of range')
            return 0
        cur = 1
        temp = self.point
        while cur !=index:
            cur = cur+1
            temp = temp.next
        return temp.items






s = Slist()
s.s_init(1)
s.add_head(2)
s.add_head(3)
s.add_head(4)
s.add_head(5)
s.add_head(6)
# s.back_Slist(2)
# s.back_Slist(3)
# s.inster(3,'a')
# s.change(3,1)
# s.delete(3)
# print('6:',s.select(1))


s1 = Slist()
s1.s_init('a')
s1.add_head('b')
s1.add_head('c')
s1.add_head('d')
s1.add_head('e')
s1.add_head('f')

s.get_data()
print('len:',s.get_length())
s1.get_data()
print('s1len:',s1.get_length())
temp = s.point
while temp.next:
    temp = temp.next
temp.next = s1.point

s1.get_data()
print('S1len:',s1.get_length())
s.get_data()
print('NEWs1len:',s.get_length())


