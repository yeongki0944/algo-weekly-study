import sys


class Stack:
    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self, item):
        self.stack.append(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return False
        else:
            self._size -= 1
            return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return self._size

    # 0 - True
    def is_empty(self):
        return self._size == 0


stack = Stack()
result = 0
cmd = sys.stdin.readline()

for i in range(len(cmd)):
    if cmd[i] == '(':
        stack.push('(')
    elif cmd[i] == ')' and cmd[i-1] == '(':
        stack.pop()
        result += stack.size()
    elif cmd[i] == ')':
        stack.pop()
        result += 1


print(result)



