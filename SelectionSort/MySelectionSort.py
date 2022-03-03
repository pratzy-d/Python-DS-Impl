#https://www.youtube.com/watch?v=5KjapFQNxUo
#search from the beginning, find the smallest and swap it with the 1st position
#continue like this

def selectionSort(data):
    for i in range(0, len(data), 1):
        minIndex = i
        for j in range(i+1, len(data), 1):
            if (data[j]<data[minIndex]):
                minIndex = j
        minIndexFound = False
        temp = data[i]
        data[i] = data[minIndex]
        data[minIndex] = temp
        print(data)

data = [5, 9, 3, 19, 11, 1, 2]
selectionSort(data)
print(data)