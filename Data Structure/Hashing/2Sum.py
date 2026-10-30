def two_sum(nums, target):
    seen = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 7, 11, 15]
k=9

print(two_sum(nums,k))

"""
Outpput: [0, 1]


"""

