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
print("Maximum contiguous product is", maximum_subarray_product(a))

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