from collections import Counter   
class Solution:
    def majorityElement(self, nums):
        ans=Counter(nums)
        n=len(nums)
        for k,v in ans.items():
            if v>n/2:
                return k
        return

s=Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums)) 

"""
output:  2

The majority element is the element that appears more than ⌊n / 2⌋ times.

"""
