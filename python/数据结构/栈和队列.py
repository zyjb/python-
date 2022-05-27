# class Stack(object):
#     def __init__(self):
#         self.stack = []
#
#
# class S(object):
#     def __init__(self):
#         self.stack = Stack()
#         self.index = 0
#
#     def push_in(self,value:int):
#         if isinstance(value,int):
#             self.stack.stack.append(value)
#             self.index += 1
#         else:
#             print('传入对象只能是int，不能是{}'.format(type(value)))
#
#     def put_out(self):
#         print(self.stack.stack[len(self.stack.stack)-1])
#         self.stack.stack = self.stack.stack[0:len(self.stack.stack)-1]
#
#     def print_(self):
#         print(self.stack.stack)
# s = S()
# s.push_in(1)
# s.push_in(2)
# s.push_in(3)
# s.push_in(4)
# s.put_out()
# s.put_out()
# s.print_()


class Queue(object):
    def __init__(self):
        self.queue =[]

class T(object):
    def __init__(self):
        queue = Queue()
        self.queue =  queue.queue
        self.index = 0

    def append(self,value):
        self.queue.append(value)
        self.index+=1

    def delete(self):
        print(self.queue[0])
        self.queue=self.queue[1:]


    def print_(self):
        print(self.queue)


t = T()
t.append(1)
t.append(2)
t.append(3)
t.append('a')
t.delete()
t.print_()