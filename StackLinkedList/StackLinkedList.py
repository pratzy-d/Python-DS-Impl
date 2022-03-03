class Node:
    def __init__(self, value):
        self.value =  value
        self.next =  None

class StackLinkedList:
    def __init__(self):
        self.Root = Node("Root")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        val = ""
        while cur:
            val += str(cur.value) + "->"
            cur = cur.next
        return val[:-3]
    
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Not found")
        return self.head.next.value

    def push(self, value):
        newNode = Node(value)
        self.Root.next = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        removeNode = self.Root.next
        self.Root.next=self.Root.next.next
        self.size -= 1
        return removeNode.value

if __name__ == "__main__":
    stack = Stack()
    for i in range (1,11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1,6):
        remove = stack.pop()
        print(f"Stack: {remove}")
    print(f"Stack: {stack}")

