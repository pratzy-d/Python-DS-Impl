class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueLinkedList:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, val):
        newNode = Node(val)

        if self.front == None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def DeQueue(self):
        if self.isEmpty():
            return

        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

        