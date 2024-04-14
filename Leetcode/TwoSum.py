# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you 
# may not use the same element twice.
# You can return the answer in any order.

# def TwoSum(nums, target):
#     for num in nums:
# l = [1,2,3,4,5]
# target = 7, index = l[2] + l[3], l[1] + l[4], (2, 3) & (1, 4)


def two_sum(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
