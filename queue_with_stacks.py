import sys

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

class Queue:
    def __init__(self):
        self.stack = Stack()
        self.reverse_stack = Stack()

    def enqueue(self, item):
        self.stack.push(item)
        self.reverse_stack.items = self.reverse(self.stack)

    def dequeue(self):
        self.reverse_stack.items.pop()
        self.stack.items = self.reverse(self.reverse_stack)

    def reverse(self, stack):
        return list(reversed(stack.items))

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.stack.items)
print(queue.reverse_stack.items)

queue.dequeue()
print(queue.stack.items)

