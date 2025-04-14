"""
Maximum Frequency Stack
"""

from collections import defaultdict, deque


class FreqStack:
    def __init__(self):
        self.val_to_freq = defaultdict(int)
        self.freq_to_stack = defaultdict(deque)
        self.max_freq = 0

    def push(self, val):
        freq = self.val_to_freq[val] + 1
        self.val_to_freq[val] = freq
        self.max_freq = max(self.max_freq, freq)
        self.freq_to_stack[freq].append(val)

    def pop(self):
        val = self.freq_to_stack[self.max_freq].pop()
        self.val_to_freq[val] -= 1

        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1

        return val


freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
