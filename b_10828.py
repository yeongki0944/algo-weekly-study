import sys

class Stack:
    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self, item):
        self.stack.append(item)
        self._size += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            self._size -= 1
            return self.stack.pop()


    def top(self):
        if self._size >= 1:
            return self.stack[-1]
        else:
            return -1

    def size(self):
        return self._size

    def empty(self):
        return int(self._size == 0)


# N = map(int, input())
# 이건 왜 에러가 나지?
N = int(sys.stdin.readline())


stack = Stack()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.push(cmd[1])

    elif cmd[0] == "pop":
        print(stack.pop())

    elif cmd[0] == "top":
        print(stack.top())

    elif cmd[0] == "size":
        print(stack.size())

    elif cmd[0] == "empty":
        print(stack.empty())



