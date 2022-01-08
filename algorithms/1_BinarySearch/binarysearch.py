from util import time_it

# time complexity: O(log n)
# space complexity: O(1)

# @time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

# @time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

# @time_it
# my implementation for prob 2 -- the least efficient
def binary_search_for_all_occurences(numbers_list, number_to_find, left_index, right_index, result=[]):
    if right_index < left_index:
        return result

    mid_index = (left_index + right_index) // 2

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        result.append(mid_index)
        result_1 = binary_search_for_all_occurences(numbers_list, number_to_find, mid_index + 1, right_index, result)
        result_2 = binary_search_for_all_occurences(numbers_list, number_to_find, left_index, mid_index - 1, result)
        result = set(result_1).union(set(result_2))
        return result

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_for_all_occurences(numbers_list, number_to_find, left_index, right_index, result)

@time_it
# the given solution for prob 2 -- not the most efficient
def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

@time_it
def find_all_efficient(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    result = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            # return mid_index
            result.append(mid_index)
            mid_left = mid_index - 1
            mid_right = mid_index + 1
            while left_index <= mid_left:
                if numbers_list[mid_left] == number_to_find:
                    result.append(mid_left)
                else:
                    break
                mid_left = mid_left - 1
            
            while right_index >= mid_right:
                if numbers_list[mid_right] == number_to_find:
                    result.append(mid_right)
                else:
                    break
                mid_right = mid_right + 1
            
            return sorted(result)

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return result


if __name__ == '__main__':
    '''
    numbers_list_1 = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find_1 = 80

    index_1 = binary_search_recursive(numbers_list_1, number_to_find_1, 0, len(numbers_list_1)-1)
    print(f"Number found at index {index_1} using binary search")

    print("\n- - - - - - - - - - - - - - - - -\n")
    '''

    # exercise prob 1)
    # ans: because binary search is for only sorted arrays
    # (the given list [1,4,6,9,10,5,7] is not sorted,
    #  so if it tries to find 5,
    #  it will search [1, 4, 6] because 5 < 10,
    #  which leads to returning -1)

    # exercise prob 2) Find index of all the occurances of a number from sorted list
    numbers_list_2 = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find_2 = 15

    index_2 = binary_search_for_all_occurences(numbers_list_2, number_to_find_2, 0, len(numbers_list_2)-1)
    print(f"Number found at index {index_2} using my first least efficient way")

    index_s = find_all_occurances(numbers_list_2, number_to_find_2)
    print(f"Number found at index {index_s} using the given solution")

    index_3 = find_all_efficient(numbers_list_2, number_to_find_2)
    print(f"Number found at index {index_3} using my new efficient way")
    