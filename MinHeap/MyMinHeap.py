#YouTube - https://www.youtube.com/watch?v=hkyzcLkmoBY

def min_heapify(list, pos):
    left = findLeft(pos)
    right = findRight(pos)

    if (left < len(list) and list[left] < list[pos]):
        smallestPos = left
    else:
        smallestPos = pos

    if (right < len(list) and list[right] < list[smallestPos]):
        smallestPos = right

    if (smallestPos != pos):
        list[pos], list[smallestPos] = list[smallestPos], list[pos]
        min_heapify(list, smallestPos)

def findLeft(pos):
    return 2*pos + 1;

def findRight(pos):
    return 2*pos + 2;

def buildMinHeap(list):
    node = int((len(list)//2) - 1)

    for i in range(node, -1, -1):
        min_heapify(list, i)

mainList = [9, 8, 7, 4, 3, 19, 1]
buildMinHeap(mainList)
print(mainList)