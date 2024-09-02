def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr[n-1]
        left = []
        right = []
        for i in range (0, n-1):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
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
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        # Add any remaining elements from the left or right half
        sorted_arr.extend(left[i:])
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
    for i in range (len(count_arr)):
        sorted_arr += [i] * count_arr[i]

    return sorted_arr

a = [3, 5, 2, 4, 5, 2, 1, 8, 9, 5]
print(counting_sort(a))