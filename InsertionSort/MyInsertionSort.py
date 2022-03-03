#YouTube https://www.youtube.com/watch?v=K0zTIF3rm9s

def insertionSort(list):
    for i in range(1, len(list), 1):
        for j in range (i, 0, -1):
            if list[j] < list [j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp

list = [78, 38, 1, 87, 23]
insertionSort(list)

for item in list:
    print(item)