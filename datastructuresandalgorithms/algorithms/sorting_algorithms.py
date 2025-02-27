def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr[n-1]
        left = []
        right = []
        for j in range (0, n-1):
            if arr[j] <= pivot:
                left.append(arr[j])
            else:
                right.append(arr[j])
        sorted_arr = quick_sort(left) + [pivot] + quick_sort(right)
        return sorted_arr
    
a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
# print(quick_sort(a))

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    elif n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        left = merge_sort(arr[:n//2])
        right = merge_sort(arr[n//2:])
        
        # Merge the two sorted halves
        sorted_arr = []
        j, j = 0, 0
        
        while j < len(left) and j < len(right):
            if left[j] < right[j]:
                sorted_arr.append(left[j])
                j += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        # Add any remaining elements from the left or right half
        sorted_arr.extend(left[j:])
        sorted_arr.extend(right[j:])

        return sorted_arr
    
a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
# print(merge_sort(a))

import heapq

def heap_sort(arr):
    max_heap = []
    sorted_arr = []
    
    for num in arr:
        heapq.heappush(max_heap, -num)
    
    while max_heap:
        max_element = -heapq.heappop(max_heap)
        sorted_arr.append(max_element)
    
    return sorted_arr[::-1]

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
# print(heap_sort(a))

def counting_sort(arr):
    m = max(arr)
    count_arr = [0] * (m + 1)

    for num in arr:
        count_arr[num] = count_arr[num] + 1

    sorted_arr = []
    for j in range (len(count_arr)):
        sorted_arr += [j] * count_arr[j]

    return sorted_arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(counting_sort(a))

def bubble_sort(arr):
    n = len(arr)
    for i in range (0, n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr [j+1], arr[j]
    return arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(bubble_sort(a))

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):  
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr [min_index], arr[i]
    return arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(selection_sort(a))

def insertion_sort(arr):
    n = len(arr)
    return arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(insertion_sort(a))

def shell_sort(arr):
    n = len(arr)
    return arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(shell_sort(a))

def bucket_sort(arr):
    n = len(arr)
    return arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(bucket_sort(a))

def radix_sort(arr):
    m = max(arr)
    sorted_arr = []
    return sorted_arr

a = [3, 50, 207, 4, 555, 2, 17, 8, 9, 5]
print(radix_sort(a))
