def two_sums(nums, target):
    '''
    need to return index of elements which sums up to the target
    so we require index and element both, better to use empty dict for this task
    we can subtract element from target to know the difference of it
    and accordingly checks if difference is present in the dict
    if it is present it means that dict key and current loop's element is the sum of the target
    so we just need indices of both elements
    from loop, i is the index and from dict, value of that difference(key) is the index 
    '''
    # so we first declare an empty dictonary
    num_indices = {}
    result = []
    for i, num in enumerate(nums):
        difference = target - num
        if difference in num_indices:
            result.append([num_indices[difference], i])
        num_indices[num] = i
    return result
nums = [1, 2, 4, 5, 7, 9, 3, 11, 5, 1]
target = 6
print(two_sums(nums, target))