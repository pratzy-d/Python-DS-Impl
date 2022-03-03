#YouTube - https://www.youtube.com/watch?v=ea8BRGxGmlA

class MyHashTable:
    def __init__(self):
        self.MAX = 100
        self.hash_table = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_value = 0;
        for c in key:
            hash_value += ord(c)
        return hash_value%self.MAX

    # def add(self, key, val):
    #     hash_index = self.get_hash(key)
    #     self.hash_table[hash_index] = val

    # def get(self, key):
    #     hash_index = self.get_hash(key)
    #     return self.hash_table[hash_index]

    # def delete(self, key):
    #     hash_index = self.get_hash(key)
    #     self.hash_table[hash_index] = None

    def __setitem__(self, key, val):
        hash_index = self.get_hash(key)
        self.hash_table[hash_index] = val

    def __getitem__(self, key):
        hash_index = self.get_hash(key)
        return self.hash_table[hash_index]

    def __delitem__(self, key):
        hash_index = self.get_hash(key)
        self.hash_table[hash_index] = None

    def print_all_values(self):
        for val in self.hash_table:
            if val != None:
                print(val)


ht = MyHashTable()

ht["C-0350-15"] = "Akankshya Mohanty"
ht["C-0550-15"] =  "Anandi Jain"
ht["C-0650-18"] =  "Manasi Mohanty"
ht["C-0355-15"] =  "Prateekshya Mohanty"
ht["C-0911-15"] =  "Naysa Mohanty"
ht["C-0200-15"] =  "Sara Luthra "
print("Initial Values are =>>>")
ht.print_all_values()

print("Retrieved value is", ht["C-0200-15"])
del ht["C-0911-15"]
print("Final Values are =>>>")
ht.print_all_values()