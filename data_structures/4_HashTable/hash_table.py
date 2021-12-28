# [ array ]
import os
stock_price_list = []
abs_path = os.path.dirname(os.path.abspath(__file__))
file_name = abs_path + '/stock_prices.csv'
with open(file_name, "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price_list.append([day, price])

print(stock_price_list)
# to find stock price on march 9
for element in stock_price_list:
    if element[0] == 'march 9':
        print(element[1])
# --> complexity of search using a list is O(n)


# [ dictionary (hashmap) ]
stock_price_dict = {}
with open(file_name, "r") as f:
    for line in f:
        tokens = line.split(',')
        stock_price_dict[tokens[0]] = float(tokens[1])

print(stock_price_dict)
# to find stock price on march 9
stock_price_dict['march 9']
# --> complexity of search using a dictionaty is O(1)


# [ Implement Hash Table ]

# hash function converts your string key into an index into array
# hash functions 1) using ASCII numbers
#               --> add all ASCII numbers of string key and
#                   reduce number using mod (to get indexes less than array size)
#                   (e.g. if array size is 10, mod(609, 10) -> 9

# ord() returns an integer representing the Unicode character
# ASCII encoding : ascii value to binary (Western characters)
# each character becomes 8bits/1byte of binary data
# there are also Unicode encodings ...

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 310
    print(t["march 6"])
    print(t["march 10"])
    del t["march 6"]
    print(t["march 6"])

# lookup by key: O(1) on average
# insertion/deletion: O(1) on average
