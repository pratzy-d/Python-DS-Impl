#YouTube https://www.youtube.com/watch?v=hkyzcLkmoBY

def max_heapify(DataList, i):
    left = findLeft(i)
    right = findRight(i)

    if left < len(DataList) and DataList[left] > DataList[i]:
        largest = left
    else:
        largest = i

    if right < len(DataList) and DataList[right] > DataList[largest]:
        largest = right
    
    if largest != i:
        DataList[i], DataList[largest] = DataList[largest], DataList[i]
        max_heapify(DataList, largest)

def findLeft(i):
    return 2*i + 1;

def findRight(i):
    return 2*i + 2;

def build_max_heap(DataList):
    node = int((len(DataList)//2) - 1)
    for i in range(node, -1, -1):
        max_heapify(DataList, i)

mainList = [3,9,2,1,4,5]
build_max_heap(mainList)
print(mainList)