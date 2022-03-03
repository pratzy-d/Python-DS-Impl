def linearSearch(data, val):
    for i in data:
        if i == val:
            return True

    return False
    # i = 0
    # while(i < len(data)):
    #     if (data[i] == val):
    #         return True;
    #     i += 1

    # return False;

list = [78,7, 8, 9, 11, 71, 6, 23]
ret = linearSearch(list, 90)

if ret:
    print("Found")
else:
    print("Not found")