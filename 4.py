class Node:
    def __init__(self,data, nextN = None, prevN = None):
        self.data = data
        self.nref = None
        self.pref = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def unshift (self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.nref = self.head
            self.head.pref = newNode
            self.head  = newNode

    def push (self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            newNode = Node(data)
            n.nref = newNode
            newNode.pref = n

    def shift (self):
        if self.head is None:
            print("The list is empty")
        elif self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    def pop (self):
        if self.head is None:
            print("The list is empty")
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def printList(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nref

myList = DoubleLinkedList()

myList.push(100)

myList.push(50)

myList.unshift(20)

myList.shift()

myList.pop()

myList.printList()


