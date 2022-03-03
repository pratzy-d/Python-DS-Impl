def calculateFibonnaci(n):
    if (n == 0):
        return 0
    if (n==1):
        return 1
    else:
        return calculateFibonnaci(n-1) + calculateFibonnaci(n-2);


for i in range(10):
    print(calculateFibonnaci(i))