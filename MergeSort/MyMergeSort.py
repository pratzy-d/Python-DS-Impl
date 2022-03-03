#https://www.youtube.com/watch?v=cVZMah9kEjI
#Divide and Conquer Algorithm
#O(n * log(n)) running time

def mergeSort(data):
    if (len(data) > 1):
        #divide the array into two parts
        left_array  = data[:len(data)//2]
        right_array = data[len(data)//2:]

        mergeSort(left_array)
        mergeSort(right_array)
        print(left_array)
        print(right_array)

        l = 0
        r = 0
        k = 0
        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                data[k] = left_array[l]
                l += 1
                k += 1
            else:
                data[k] = right_array[r]
                r += 1
                k += 1
        
        while l < len(left_array):
            data[k] = left_array[l]
            l += 1
            k += 1

        while r < len(right_array):
            data[k] = right_array[r]
            r += 1
            k += 1

data = [78, 7, 99, 11, 43, 5, 6, 2]
mergeSort(data)
print(data)