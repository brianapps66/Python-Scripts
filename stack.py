import sys
#Implement a stack with push and pop functions

class Stack:
    def __init__(self):
        self.items = []
        self.min = sys.maxsize      #for O(1) finding of minimum element

    def push(self, item):
        if item < self.min:
            self.min = item
        return self.items.append(item)

    def pop(self):
        result = self.items.pop()
        if result is self.min:
            self.min = find_min(self)
        return result

    def is_empty(self):
        if len(self.items) is 0:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def duplicate(self):
        self.items.append(self.peek())

    def swap(self):
        temp = self.pop()
        temp2 = self.pop()
        self.items.append(temp)
        self.items.append(temp2)

    def rotate_left(self):
        self.items.insert(len(self.items)-1, self.items.pop(0))

    def rotate_right(self):
        self.items.insert(0, self.items.pop())

def find_min(stack):
    min = stack.peek()
    for item in stack.items:
        if item < min:
            min = item
    return min

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

print(stack.items)
stack.pop()
print(stack.items)
print(stack.peek())
print(stack.is_empty())
#stack.duplicate()
print(stack.items)
stack.swap()
print(stack.items)
stack.rotate_right()
stack.rotate_right()
stack.rotate_right()
print(stack.items)
print(find_min(stack))
print(stack.min)
stack.pop()
print(stack.items)
print(stack.min)
