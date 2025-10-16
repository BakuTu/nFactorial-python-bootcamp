class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, i):
        if i < 0 or i >= self.size:
            print("Index out of range")
            return

        if i == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            else:
                current = self.head
                for _ in range(i - 1):
                    current = current.next
                current.next = current.next.next
                if i == self.size - 1:
                    self.tail = current
            self.size -= 1
    def insert(self, i, data):
        if i < 0 or i > self.size:
            print("Index out of range")
            return

        new_node = Node(data)
        if i == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif i == self.size:
            self.tail.next = new_node
        else:
            current = self.head
            for _ in range(i - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def __len__(self):
        return self.size

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
