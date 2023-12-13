class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. No top element.")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# 예시 코드
stack = Stack()

# push
stack.push(1)
stack.push(2)
stack.push(3)

# pop
print("Popped:", stack.pop())

# top
print("Top:", stack.top())

# size
print("Size:", stack.size())

# empty
print("Is Empty:", stack.is_empty())
