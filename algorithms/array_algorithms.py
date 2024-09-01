# O(n)
# kadene
def maximum_subarray_sum(arr):
    max_current = max_global = arr[0]

    # print(max_current)
    # print(max_global)

    for i in range(1, len(arr)):
        if max_current + arr[i] > arr[i]:
            max_current = max_current + arr[i]
        else:
            max_current = arr[i]
        # print(max_current)
        if max_current > max_global:
            max_global = max_current
        # print(max_global)
    return max_global

a = [-2, 1, 3, -7, 3, 1, 1, 2, 1]
# print("Maximum contiguous sum is", maximum_subarray_sum(a))

# O(n)
# kadene
def maximum_subarray_product(arr):
    max_so_far = min_ending_here = max_ending_here = arr[0]

    for i in range(1, len(arr)):
        temp_max = max(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
        min_ending_here = min(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
        # print("min",min_ending_here)
        max_ending_here = temp_max
        # print("max",max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
        # print("msf", max_so_far)

    return max_so_far

a = [1, -2, -3, 0, 7, -8, -2]
# print("Maximum contiguous product is", maximum_subarray_product(a))

# O(n)
def find_missing_number(arr):
    # or with sum(arr)
    sum = 0
    for i in arr:
        sum += i
    full_sum = (len(arr)+1) * (len(arr)+2) / 2
    return full_sum - sum

a = [1, 2, 3, 5, 7, 6, 8]
# print(find_missing_number(a))

# O(n)
def equilibrium_index(arr):
    if len(arr) < 3:
        return -1
    
    left = 0
    pivot = 0
    right = sum(arr[1:])

    while pivot < len(arr) - 1 and right != left:
        pivot += 1
        right -= arr[pivot]
        left += arr[pivot - 1]
    
    if left == right:
        return pivot
    else:
        return -1

a = [1, 7, 3, 6, 5, 6]
# print(equilibrium_index(a))

# O(n)
def array_leaders(arr):
    ans = [arr[-1]]
    n = len(arr)
    max_right = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            ans.append(arr[i])
            max_right = arr[i]
    return ans

a = [16, 17, 4, 3, 5, 2]
# print(array_leaders(a))

# O(n)
def rotate_k_times(arr, k):
    n = len(arr)
    k = k % n
    rotated_arr = arr[(n - k): n] + arr[:(n - k)]
    return rotated_arr

a = [16, 17, 4, 3, 5, 2]
# print(rotate_k_times(a, 1))
# print(rotate_k_times(a, 2))
# print(rotate_k_times(a, 3))
# print(rotate_k_times(a, 7))

def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

a = [16, 17, 4, 3, 5, 2]
# print(kth_smallest(a, 3))