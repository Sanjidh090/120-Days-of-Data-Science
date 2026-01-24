x = [1,2,3,4,5,6,6,7,1,8,9,9,10]
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = binary_search(x, 7)
print("Element found at index:", result)