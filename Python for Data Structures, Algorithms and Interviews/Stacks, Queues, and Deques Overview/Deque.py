



class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()

d.items = [1, 2, 3, 4, 'str', True, 20.5]
d.addFront("Front")
d.addRear("Rear")
d.removeFront()
d.removeRear()


print(d.items)
print(d.isEmpty())
print(d.size())
d.items = []
print(d.isEmpty())
print(d.size())