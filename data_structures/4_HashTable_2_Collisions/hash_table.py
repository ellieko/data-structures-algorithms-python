# Exercise: Hash Table

'''
1. [nyc_weather.csv](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv)
    contains new york city weather for first few days in the month of January.
    Write a program that can answer following,
    1. What was the average temperature in first week of Jan
    2. What was the maximum temperature in first 10 days of Jan

Figure out data structure that is best for this problem
'''
import os
temp_list = []
abs_path = os.path.dirname(os.path.abspath(__file__))
temp_file = abs_path + '/Solution/nyc_weather.csv'
with open(temp_file, "r") as f:
    for line in f:
        tokens = line.split(',')
        if tokens[0] == 'date':
            pass
        else:
            temp_list.append(int(tokens[1]))
print("\nExercise Problem 1)")
print(f"The best data structure to use here was a list\n\
because all we wanted was access of temperature elements")
print(f"The avaerage temperature in first week of Jan: \
{round(sum(temp_list[:7])/7,2)}")
print(f"The maximum temperature in first 10 days of Jan: {max(temp_list)}")


'''
2. [nyc_weather.csv](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv)
   contains new york city weather for first few days in the month of January.
   Write a program that can answer following,
    1. What was the temperature on Jan 9?
    2. What was the temperature on Jan 4?

Figure out data structure that is best for this problem
'''
temp_dict = {}
with open(temp_file, "r") as f:
    for line in f:
        tokens = line.split(',')
        if tokens[0] == 'date':
            pass
        else:
            temp_dict[tokens[0]] = int(tokens[1])
print("\nExercise Problem 2)")
print(f"The best data structure to use here was a dictionary (internally a hash table)\n\
because we wanted to know temperature for specific day, requiring key, value pair access\n\
where you can look up an element by day using O(1) complexity")
print(f"The temperature on Jan 9: {temp_dict['Jan 9']}")
print(f"The temperature on Jan 4: {temp_dict['Jan 4']}")


'''
3. [poem.txt](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/poem.txt)
   contains famous poem "Road not taken" by poet Robert Frost.
   You have to read this file in python and print every word and its count as show below.
   Think about the best data structure that you can use to solve this problem
   and figure out why you selected that specific data structure.

 'diverged': 2,
 'in': 3,
 'I': 8
'''
word_dict = {}
poem_file = abs_path + '/Solution/poem.txt'
with open(poem_file, "r") as f:
    for line in f:
        for word in line.split():
            key = word.strip('—.;,\n')
            if key in word_dict:
                word_dict[key] += 1
            else:
                word_dict[key] = 1
print("\nExercise Problem 3)")
print(f"Best data structure: Dictionary\n{word_dict}")


'''
4. Implement hash table where collisions are handled using linear probing.
   We learnt about linear probing in the video tutorial.
   Take the hash table implementation that uses chaining and modify methods to use **linear probing**.
   Keep MAX size of arr in hashtable as 10.
'''


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [(None, None) for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        if self.arr[arr_index][0] == key:
            return self.arr[arr_index][1]
        else:
            found = False
            if arr_index + 1 == self.MAX:
                idx = 0
            else:
                idx = arr_index + 1
            while (not found and idx != arr_index):
                if self.arr[idx][0] == key:
                    found = True
                    return self.arr[idx][1]
                else:
                    if idx + 1 == self.MAX:
                        idx = 0
                    else:
                        idx += 1

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h][0] in (key, None):
            self.arr[h] = (key, val)
        else:
            if h + 1 == self.MAX:
                idx = 0
            else:
                idx = h + 1
            new_idx = None
            found = False
            while not found and idx != h:
                target = self.arr[idx][0]
                if target == key:
                    found = True
                    self.arr[idx] = (key, val)
                else:
                    if target == None and new_idx == None:
                        new_idx = idx
                    if idx + 1 == self.MAX:
                        idx = 0
                    else:
                        idx += 1
            if not found:
                if new_idx == None:
                    raise Exception("Hashmap is full")
                else:
                    self.arr[new_idx] = (key, val)

    # Problem) deleted position should have (None, None) but
    #          it just deletes the one entry
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        if self.arr[arr_index][0] == key:
            del self.arr[arr_index]
        else:
            found = False
            if arr_index + 1 == self.MAX:
                idx = 0
            else:
                idx = arr_index + 1
            while (not found and idx != arr_index):
                if self.arr[idx][0] == key:
                    found = True
                    self.arr[idx] = (None, None)
                else:
                    if idx + 1 == self.MAX:
                        idx = 0
                    else:
                        idx += 1


print("\nExercise Problem 4)")
print(f"Tested fine.\n\
Even took care of the corner case that the solution didn't take care of,\n\
which is get or set item that has been stored at somewhere else when the arr[h] gets deleted.\n\
Lesson learned: use helper fuction!!!! (the current code is too hard to read)")
'''
t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
print(t.arr)
t["march 17"] = 29
print(t.arr)
t["nov 1"] = 1
print(t.arr)
t["march 33"] = 234
print(t.arr)
print(t["dec 1"])
print(t["march 33"])
t["march 33"] = 999
print(t.arr)
t["april 1"] = 87
print(t.arr)
t["april 2"] = 123
print(t.arr)
t["april 3"] = 234234
print(t.arr)
t["april 4"] = 91
print(t.arr)
t["May 22"] = 4
print(t.arr)
t["May 7"] = 47
print(t.arr)
# t["Jan 1"] = 0 --> raise exception
del t["april 2"]
print(t.arr)
'''
