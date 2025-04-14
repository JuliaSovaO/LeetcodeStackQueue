"""
Implement Queue using Stacks
"""


class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            self._transfer()
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            self._transfer()
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out

    def _transfer(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())


myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())
