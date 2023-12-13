class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("is empty")
            return False
        else:
            return self.stack.pop()

    def is_empty(self):
        if self.size() >= 1:
            return False
        else:
            return True

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]




stack = Stack()

stack.push(1)
print(stack.pop())
print(stack.pop())

