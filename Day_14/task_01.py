#Two sum
target = 26
nums = [2,7,11,15]
def two_sum(nums, target):
    num_map = {}
    for i, current in enumerate(nums):
        complement = target - current
        if complement in num_map:
            return [num_map[complement], i]
        num_map[current] = i
    return []

x = two_sum(nums, target)

if len(x) == 2:
    print(f"Indices found: {x[0]} and {x[1]}")
    print(f"{target} is consisted of {nums[x[0]]} and {nums[x[1]]}   ")
else:
    print("No two sum solution found.")
