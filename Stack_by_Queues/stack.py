"""
Implement Stack using Queues
"""


class Queue:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.push(x)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop()

    def top(self):
        return self.q1.peek()

    def empty(self):
        return self.q1.empty()


obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)
