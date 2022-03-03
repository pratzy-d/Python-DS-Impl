#YouTube video explaining HeapClass
#https://www.youtube.com/watch?v=hkyzcLkmoBY

class MyMinHeap:

    def __init__(self, capacity):
        self.heap = [0] * capacity
        self.capacity =  capacity
        self.size = 0

    def getParentIndex(self, index):
        return ((index-1)//2)

    def getLeftIndex(self, index):
        return (2*index+1)

    def getRightIndex(self, index):
        return (2*index+2)

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightIndex(index) < self.size

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.heap[index2]
        self.heap[index2] = self.heap[index1]
        self.heap[index1] = temp

    def insert(self, data):
        if (self.isFull()):
            raise("Heap is Full")
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)

    def deleteMin(self):
        if (self.size == 0):
            raise("The heap is empty")

        data = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heapifyDown(0)
        return data
        
    def heapifyUp(self, index):
        if (self.hasParent(index)) and (self.heap[self.getParentIndex(index)] > self.heap[index]):
            self.swap(self.getParentIndex(index), index)
            #keep heapifying up until you reach the root node (which doesn't have parent node)
            self.heapifyUp(self.getParentIndex(index))

    def heapifyDown(self, index):
            print("before heapify", self.heap)
            smallerChildIndex = index
            if (self.hasLeftChild(index) and self.heap[self.getLeftIndex(index)] < self.heap[index]):
                smallerChildIndex = self.getLeftIndex(index)
            if (self.hasRightChild(index) and self.heap[self.getRightIndex(index)] < self.heap[smallerChildIndex]):
                smallerChildIndex = self.getRightIndex(index)
            
            if (index != smallerChildIndex):
                self.swap(index, smallerChildIndex)
                self.heapifyDown(smallerChildIndex)

    def printHeap(self):
        for i in range(0, self.size, 1):
            print(self.heap[i])
            
        
minHeap = MyMinHeap(10)
minHeap.insert(15)
minHeap.insert(18)
minHeap.insert(79)
minHeap.insert(125)
minHeap.insert(35)
minHeap.insert(2)
minHeap.insert(16)
minHeap.insert(100)

minHeap.printHeap()

minHeap.deleteMin()
print("Post Pop, the Heap looks like as ...")
minHeap.printHeap()

minHeap.deleteMin()
print("Post Pop, the Heap looks like as ...")
minHeap.printHeap()

minHeap.deleteMin()
print("Post Pop, the Heap looks like as ...")
minHeap.printHeap()