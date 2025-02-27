def linear_search(collection, target):
    n = len(collection)
    for i in range(n):
        if collection[i] == target:
            return i
    return False

a = [2, 3, 4, 10, 40]
result = linear_search(a, 10)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)


def binary_search(sorted_list, target):
    right = len(sorted_list) -1
    left = 0
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_list[mid] == target:
            return mid
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

a = [2, 3, 4, 10, 40]
print(binary_search(a, 10))


def ternary_search(sorted_list, target):
    right = len(sorted_list) -1
    left = 0
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if sorted_list[mid1] == target:
            return mid1
        if sorted_list[mid2] == target:
            return mid2
        elif target < sorted_list[mid1]:
            right = mid1 - 1
        elif target > sorted_list[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 -1
    return -1

a = [2, 3, 4, 10, 40]
print(ternary_search(a, 10))

def fibonacci_search():
    pass

def depth_first_search_graph():
    pass

def breadth_first_search_graph():
    pass