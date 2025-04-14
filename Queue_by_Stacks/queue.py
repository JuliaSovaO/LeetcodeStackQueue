"""
Implement Queue using Stacks
"""


class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0


class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x):
        self.stack_in.push(x)

    def pop(self):
        if self.stack_out.empty():
            self._transfer()
        return self.stack_out.pop()

    def peek(self):
        if self.stack_out.empty():
            self._transfer()
        return self.stack_out.peek()

    def empty(self):
        return self.stack_in.empty() and self.stack_out.empty()

    def _transfer(self):
        while not self.stack_in.empty():
            self.stack_out.push(self.stack_in.pop())


myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
