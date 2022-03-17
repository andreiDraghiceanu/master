



class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

print(q.size())
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(9)
q.enqueue(10)
q.enqueue(True)
q.enqueue("String1")
q.dequeue()
print(q.items)
print(q.size())