#find the target


def find_two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []

# Example input
nums = [2, 7, 11, 15]
target = 9

# Find the two integers that sum to the target
result = find_two_sum(nums, target)

# Print the output
print(result)