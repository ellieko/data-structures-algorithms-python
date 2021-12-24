# 1. expenses
print("\n##### 1. Expenses #####")
expense = [2200, 2350, 2600, 2130, 2190]

print(f"1) In Feb, you spent extra \"{expense[1]-expense[0]}\" \
compare to Jan.")

print(f"2) Total expense in first quarter is \
\"{expense[0]+expense[1]+expense[2]}\".")

print(f"3) Is there any month you spent exactly $2000?\n\
   Ans: {any([x for x in expense if x == 2000])}")

expense.append(1980)
print(f"4) Now expense of June is added, it is \"{expense[5]}\"")

print(f"5) The expense of April was {expense[3]}, but")
expense[3] = expense[3]-200
print(f"   she returned one item, which costs $200, \
so it is updated to \"{expense[3]}\".")


# 2. marvel
print("\n##### 2. Marvel #####")
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(f"1) Length of the list is \"{len(heros)}\".")

heros.append('black panther')
print(f"2) Added black panther at the end of the list: {heros}")

heros.remove('black panther')
heros.insert(3, 'black panther')
print(f"3) After hulk, need black panther: {heros[:]}")

heros[1:3] = ['doctor stange']
print(f"4) Removed thor and hulk and added doctor strage: {heros[:]}")

heros.sort()
print(f"5) Sort the list: {heros}")

# 3. odd_numbers
print("\n##### 3. Odd number list #####")


def odd_between_1_and_max(max):
    return [i for i in range(1, max+1) if i % 2 == 1]


m = int(input("Type max number for your list: "))
list = odd_between_1_and_max(m)
print(f"Your list is {list}")
