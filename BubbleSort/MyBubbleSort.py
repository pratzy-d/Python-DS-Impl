#YouTube https://www.youtube.com/watch?v=Vca808JTbI8

def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range (0, i, 1):
            if nums[j+1] < nums[j]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp 


list = [19, 7, 5, 18, 11, 23, 45, 1]
bubbleSort(list)
for val in list:
    print(val)