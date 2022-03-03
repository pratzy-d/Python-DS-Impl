#YouTube Link https://www.youtube.com/watch?v=DE-ye0t0oxE
import mltools as ml

def binarySearch(list, val):
    lb = 0
    ub = len(list) - 1

    while(lb <= ub):
        mid = (lb+ub)//2
        if (list[mid] == val):
            return True;
        else:
            if (val < list[mid]):
                ub =  mid
            else:
                lb = mid

    return False;

data = [3, 8, 9, 11, 12, 56, 78, 98]

if (binarySearch(data, 12) == True):
    print("Its found")
else:
    print("NOT FOUND")