class HashTable:
    def __init__(self):
        self.HashTable = [None] * 10
        self.popIndex = 0
        self.size = 0

    def getHashCode(self, val):
        asciiValue = 0

        for c in val:
            asciiValue += ord(c)

        return asciiValue%10

    def setValue(self, val):
        index = self.getHashCode(val)

        #check in the HashTable if it is already present
        #if not present, then we can store it
        if self.HashTable[index] == None:
            self.HashTable[index] = val
            self.size += 1
        else:
            #iterate
            print("Linear Probing")

    def getValue(self, val):
        index = self.getHashCode(val)

        return self.HashTable[index];

    def getValueAtIndex(self, index):
        return self.HashTable[index]

    def getSize(self):
        return self.size

class Iterator:
    def __init__(self, h):
        self.iterator = 0
        self.h = h

    def ITER_BEGIN(self):
        i = 0
        N = self.h.getSize()
        while (i < self.h.getSize()):
            if (self.h.getValueAtIndex(i%N) != None):
                self.iterator = i
                return i  
            i += 1

        self.iterator = -1
        return -1

    def ITER_PAST_END(self):
        i = 0
        while (i%self.h.getSize() and i < self.h.getSize()):
            if (self.h.getValueAtIndex() != None):
                return False
            i += 1
        return True

    def ITER_KEY(self):
        if self.ITER_PAST_END() == False:
            return self.h.getValueAtIndex(self.iterator)
        else:
            raise("The HashTable is empty")

    def ITER_NEXT(self):
        i = 0
        N = self.h.getSize()
        while (self.h.getValueAtIndex((self.iterator + i)%N) != None and i < N):
            i += 1