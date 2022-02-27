
# average time complexity: O(nlogn)
# worst time complexity: O(n^2)
# space complexity: O()

# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


# implementation of quick sort in python using lumoto partition scheme (exercise prob)

def quick_sort_lumoto(elements, low, high):
    pass

def partition_lumoto(elements, low, high):
    pivot_index = high
    pivot = elements[high]
    while low != high :
        while low < len(elements) and elements[low] <= pivot:
            low += 1
        if low < len(elements):
            high = low
        while elements[high] > pivot:
            high += 1
        if low < high:
            swap(low, high, elements)
    return pivot_index


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    # quick_sort(elements, 0, len(elements)-1)
    print(elements)
    partition_lumoto(elements, 0, len(elements)-1)
    print(elements)
    #partition_lumoto(elements, 1)
    print(elements) 

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array by hoare partition: {elements}')
        #quick_sort_lumoto(elements, 0, len(elements)-1)
        #print(f'sorted array by lumoto partition: {elements}')